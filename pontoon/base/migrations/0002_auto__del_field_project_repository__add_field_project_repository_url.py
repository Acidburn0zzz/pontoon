# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.repository'
        db.delete_column('base_project', 'repository')

        # Adding field 'Project.repository_url'
        db.add_column('base_project', 'repository_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Project.repository'
        db.add_column('base_project', 'repository',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Deleting field 'Project.repository_url'
        db.delete_column('base_project', 'repository_url')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'base.entity': {
            'Meta': {'object_name': 'Entity'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Project']"}),
            'source': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'string': ('django.db.models.fields.TextField', [], {})
        },
        'base.locale': {
            'Meta': {'object_name': 'Locale'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'base.project': {
            'Meta': {'object_name': 'Project'},
            'external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_audience': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'info_brief': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'info_locales': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'info_metrics': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'links': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'locales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['base.Locale']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'repository_path': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'repository_type': ('django.db.models.fields.CharField', [], {'default': "'File'", 'max_length': '20'}),
            'repository_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'transifex_project': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'transifex_resource': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        },
        'base.subpage': {
            'Meta': {'object_name': 'Subpage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Project']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'base.translation': {
            'Meta': {'object_name': 'Translation'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Entity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Locale']"}),
            'string': ('django.db.models.fields.TextField', [], {})
        },
        'base.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'svn_password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'svn_username': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'transifex_password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'transifex_username': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['base']