# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Agency.registration'
        db.add_column('agencies_agency', 'registration',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, unique=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Agency.registration'
        db.delete_column('agencies_agency', 'registration')


    models = {
        'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['agencies']