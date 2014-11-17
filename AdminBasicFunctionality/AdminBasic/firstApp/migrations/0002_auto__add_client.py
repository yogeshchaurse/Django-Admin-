# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'firstApp_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['firstApp.ClientIndustry'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('mailing_street', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mailing_street2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mailing_city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mailing_zip', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'firstApp', ['Client'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'firstApp_client')


    models = {
        u'firstApp.client': {
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['firstApp.ClientIndustry']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'mailing_city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mailing_street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mailing_street2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mailing_zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'firstApp.clientindustry': {
            'Meta': {'object_name': 'ClientIndustry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['firstApp']