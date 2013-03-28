# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Product'
        db.delete_table('software_product')

        # Deleting model 'AgencyProduct'
        db.delete_table('software_agencyproduct')

        # Deleting model 'ProductType'
        db.delete_table('software_producttype')

        # Adding model 'SoftwareType'
        db.create_table('software_softwaretype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('software', ['SoftwareType'])

        # Adding model 'AgencySoftware'
        db.create_table('software_agencysoftware', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('software', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['software.Software'])),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('software', ['AgencySoftware'])

        # Adding model 'Software'
        db.create_table('software_software', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('software_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['software.SoftwareType'])),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal('software', ['Software'])


    def backwards(self, orm):
        # Adding model 'Product'
        db.create_table('software_product', (
            ('product_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['software.ProductType'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True)),
        ))
        db.send_create_signal('software', ['Product'])

        # Adding model 'AgencyProduct'
        db.create_table('software_agencyproduct', (
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['software.Product'])),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('software', ['AgencyProduct'])

        # Adding model 'ProductType'
        db.create_table('software_producttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=128, unique=True)),
        ))
        db.send_create_signal('software', ['ProductType'])

        # Deleting model 'SoftwareType'
        db.delete_table('software_softwaretype')

        # Deleting model 'AgencySoftware'
        db.delete_table('software_agencysoftware')

        # Deleting model 'Software'
        db.delete_table('software_software')


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
        },
        'software.agencysoftware': {
            'Meta': {'ordering': "['software']", 'object_name': 'AgencySoftware'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['agencies.Agency']"}),
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'software': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['software.Software']"})
        },
        'software.software': {
            'Meta': {'ordering': "['label']", 'object_name': 'Software'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'software_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['software.SoftwareType']"})
        },
        'software.softwaretype': {
            'Meta': {'ordering': "['label']", 'object_name': 'SoftwareType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['software']