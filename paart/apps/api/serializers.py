from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from rest_framework import serializers

from agencies.models import Agency


class AgencySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Agency
