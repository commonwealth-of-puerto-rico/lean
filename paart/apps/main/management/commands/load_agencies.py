import csv
from optparse import make_option

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand, CommandError

from acls.models import AccessEntry
from agencies.models import Agency
from agencies.permissions import PERMISSION_AGENCY_VIEW
from projects.permissions import (PERMISSION_PROJECT_CREATE,
    PERMISSION_PROJECT_EDIT, PERMISSION_PROJECT_DELETE, PERMISSION_PROJECT_VIEW)
from telecomm.permissions import (PERMISSION_EQUIPMENT_CREATE,
    PERMISSION_EQUIPMENT_EDIT, PERMISSION_EQUIPMENT_DELETE, PERMISSION_EQUIPMENT_VIEW)
from tools.permissions import (PERMISSION_TOOLS_PROFILE_CREATE,
    PERMISSION_TOOLS_PROFILE_EDIT, PERMISSION_TOOLS_PROFILE_DELETE,
    PERMISSION_TOOLS_PROFILE_VIEW)

GROUP_NAME = 'lean'


class Command(BaseCommand):
    args = '<input file>'

    option_list = BaseCommand.option_list + (
       make_option('--add_groups', action='store_true',
       dest='add_groups', default=False,
       help='Create the employee groups for each agency'),
       make_option('--add_acls', action='store_true',
       dest='add_acls', default=False,
       help='Grant the agency groups the necessary agency permissions.'),
    )
    help = "Read and import a list of agencies from a CSV file."

    def handle(self, *args, **options):
        try:
            input_file = args[0]
        except IndexError:
            raise CommandError('No input file.')

        self.import_csv_file(input_file)

        if options['add_groups']:
            print 'Creating groups...'
            for agency in Agency.objects.exclude(prifas__isnull=True):
                group, created = Group.objects.get_or_create(name=self.group_name_formater(agency.prifas))
            print 'Done.'

        if options['add_acls']:
            print 'Granting ACLs...'
            for agency in Agency.objects.exclude(prifas__isnull=True):
                try:
                    group = Group.objects.get(name=self.group_name_formater(agency.prifas))
                except Group.DoesNotExist:
                    pass
                else:
                    AccessEntry.objects.grant(PERMISSION_AGENCY_VIEW.stored_permission, group, agency)

                    AccessEntry.objects.grant(PERMISSION_PROJECT_CREATE.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_PROJECT_EDIT.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_PROJECT_DELETE.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_PROJECT_VIEW.stored_permission, group, agency)

                    AccessEntry.objects.grant(PERMISSION_EQUIPMENT_CREATE.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_EQUIPMENT_EDIT.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_EQUIPMENT_DELETE.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_EQUIPMENT_VIEW.stored_permission, group, agency)

                    AccessEntry.objects.grant(PERMISSION_TOOLS_PROFILE_CREATE.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_TOOLS_PROFILE_EDIT.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_TOOLS_PROFILE_DELETE.stored_permission, group, agency)
                    AccessEntry.objects.grant(PERMISSION_TOOLS_PROFILE_VIEW.stored_permission, group, agency)

            print 'Done.'

    def group_name_formater(self, prifas):
        return '{0}-{1}'.format(str(prifas).zfill(3), GROUP_NAME)

    def import_csv_file(self, input_file):
        try:
            with open(input_file, 'rb') as csvfile:
                agency_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in agency_reader:
                    agency, created = Agency.objects.get_or_create(prifas=int(row[0]), name=row[1])
                    print 'Importing agency: {1} with PRIFAS number: {0}'.format(int(row[0]), row[1])
        except IOError as exception:
            raise CommandError(unicode(exception))
