# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Participant'
        db.delete_table(u'pa_participant')

        # Removing M2M table for field user on 'Participant'
        db.delete_table('pa_participant_user')

        # Adding M2M table for field user on 'ReportingPeriod'
        db.create_table(u'pa_reportingperiod_user', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reportingperiod', models.ForeignKey(orm[u'pa.reportingperiod'], null=False)),
            ('user', models.ForeignKey(orm[u'pa.user'], null=False))
        ))
        db.create_unique(u'pa_reportingperiod_user', ['reportingperiod_id', 'user_id'])


    def backwards(self, orm):
        # Adding model 'Participant'
        db.create_table(u'pa_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reporting_period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pa.ReportingPeriod'])),
        ))
        db.send_create_signal(u'pa', ['Participant'])

        # Adding M2M table for field user on 'Participant'
        db.create_table(u'pa_participant_user', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participant', models.ForeignKey(orm[u'pa.participant'], null=False)),
            ('user', models.ForeignKey(orm[u'pa.user'], null=False))
        ))
        db.create_unique(u'pa_participant_user', ['participant_id', 'user_id'])

        # Removing M2M table for field user on 'ReportingPeriod'
        db.delete_table('pa_reportingperiod_user')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pa.activity': {
            'Meta': {'object_name': 'Activity'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pa.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pa.activityentry': {
            'Meta': {'object_name': 'ActivityEntry'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pa.Activity']"}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hour': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pa.User']"})
        },
        u'pa.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'grouping': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reporting_period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pa.ReportingPeriod']"})
        },
        u'pa.profession': {
            'Meta': {'object_name': 'Profession'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'pa.reportingperiod': {
            'Meta': {'object_name': 'ReportingPeriod'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slots_per_hour': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pa.User']", 'symmetrical': 'False'})
        },
        u'pa.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'profession': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pa.Profession']", 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['pa']