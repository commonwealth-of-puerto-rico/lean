# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductType'
        db.create_table('software_producttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('software', ['ProductType'])

        # Adding model 'Product'
        db.create_table('software_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['software.ProductType'])),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('software', ['Product'])


    def backwards(self, orm):
        # Deleting model 'ProductType'
        db.delete_table('software_producttype')

        # Deleting model 'Product'
        db.delete_table('software_product')


    models = {
        'software.product': {
            'Meta': {'ordering': "['label']", 'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['software.ProductType']"})
        },
        'software.producttype': {
            'Meta': {'ordering': "['label']", 'object_name': 'ProductType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['software']