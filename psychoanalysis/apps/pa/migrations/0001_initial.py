# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReportingPeriod'
        db.create_table(u'pa_reportingperiod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('slots_per_hour', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pa', ['ReportingPeriod'])

        # Adding model 'Category'
        db.create_table(u'pa_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reporting_period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pa.ReportingPeriod'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('grouping', self.gf('django.db.models.fields.CharField')(default='d', max_length=15)),
        ))
        db.send_create_signal(u'pa', ['Category'])

        # Adding model 'Activity'
        db.create_table(u'pa_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pa.Category'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'pa', ['Activity'])

        # Adding model 'ActivityEntry'
        db.create_table(u'pa_activityentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('hour', self.gf('django.db.models.fields.IntegerField')()),
            ('slot', self.gf('django.db.models.fields.IntegerField')()),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pa.Activity'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pa.User'])),
        ))
        db.send_create_signal(u'pa', ['ActivityEntry'])

        # Adding model 'Profession'
        db.create_table(u'pa_profession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'pa', ['Profession'])

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

        # Adding model 'User'
        db.create_table(u'pa_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('profession', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pa.Profession'], null=True, blank=True)),
        ))
        db.send_create_signal(u'pa', ['User'])

        # Adding M2M table for field groups on 'User'
        db.create_table(u'pa_user_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'pa.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'pa_user_groups', ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        db.create_table(u'pa_user_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'pa.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'pa_user_user_permissions', ['user_id', 'permission_id'])


    def backwards(self, orm):
        # Deleting model 'ReportingPeriod'
        db.delete_table(u'pa_reportingperiod')

        # Deleting model 'Category'
        db.delete_table(u'pa_category')

        # Deleting model 'Activity'
        db.delete_table(u'pa_activity')

        # Deleting model 'ActivityEntry'
        db.delete_table(u'pa_activityentry')

        # Deleting model 'Profession'
        db.delete_table(u'pa_profession')

        # Deleting model 'Participant'
        db.delete_table(u'pa_participant')

        # Removing M2M table for field user on 'Participant'
        db.delete_table('pa_participant_user')

        # Deleting model 'User'
        db.delete_table(u'pa_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table('pa_user_groups')

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table('pa_user_user_permissions')


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
        u'pa.participant': {
            'Meta': {'object_name': 'Participant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reporting_period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pa.ReportingPeriod']"}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pa.User']", 'symmetrical': 'False'})
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
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
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