# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Agency.director'
        db.add_column('agencies_agency', 'director',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'Agency.physical_address'
        db.add_column('agencies_agency', 'physical_address',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Agency.postal_address'
        db.add_column('agencies_agency', 'postal_address',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Agency.director'
        db.delete_column('agencies_agency', 'director')

        # Deleting field 'Agency.physical_address'
        db.delete_column('agencies_agency', 'physical_address')

        # Deleting field 'Agency.postal_address'
        db.delete_column('agencies_agency', 'postal_address')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'director': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'physical_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postal_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['agencies']