# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Agency.prifas'
        db.add_column('agencies_agency', 'prifas',
                      self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Agency.registration'
        db.alter_column('agencies_agency', 'registration', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, null=True))

    def backwards(self, orm):
        # Deleting field 'Agency.prifas'
        db.delete_column('agencies_agency', 'prifas')


        # User chose to not deal with backwards NULL issues for 'Agency.registration'
        raise RuntimeError("Cannot reverse this migration. 'Agency.registration' and its values cannot be restored.")

    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'director': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'physical_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postal_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prifas': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['agencies']