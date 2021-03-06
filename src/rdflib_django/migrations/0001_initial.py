# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import rdflib_django.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LiteralStatement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', rdflib_django.fields.URIField(db_index=True, max_length=500, verbose_name='Subject')),
                ('predicate', rdflib_django.fields.URIField(db_index=True, max_length=500, verbose_name='Predicate')),
                ('object', rdflib_django.fields.LiteralField(db_index=True, verbose_name='Object')),
            ],
        ),
        migrations.CreateModel(
            name='NamedGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', rdflib_django.fields.URIField(max_length=500, unique=True, verbose_name='Identifier')),
            ],
            options={
                'verbose_name': 'named graph',
                'verbose_name_plural': 'named graphs',
            },
        ),
        migrations.CreateModel(
            name='NamespaceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=50, unique=True, verbose_name='Prefix')),
                ('uri', models.CharField(db_index=True, max_length=500, unique=True, verbose_name='URI')),
                ('fixed', models.BooleanField(default=False, editable=False, verbose_name='Fixed')),
            ],
            options={
                'verbose_name': 'namespace',
                'verbose_name_plural': 'namespaces',
            },
        ),
        migrations.CreateModel(
            name='URIStatement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', rdflib_django.fields.URIField(db_index=True, max_length=500, verbose_name='Subject')),
                ('predicate', rdflib_django.fields.URIField(db_index=True, max_length=500, verbose_name='Predicate')),
                ('object', rdflib_django.fields.URIField(db_index=True, max_length=500, verbose_name='Object')),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rdflib_django.NamedGraph', verbose_name='Context')),
            ],
        ),
        migrations.AddField(
            model_name='literalstatement',
            name='context',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rdflib_django.NamedGraph', verbose_name='Context'),
        ),
        migrations.AlterUniqueTogether(
            name='uristatement',
            unique_together=set([('subject', 'predicate', 'object', 'context')]),
        ),
        migrations.AlterUniqueTogether(
            name='literalstatement',
            unique_together=set([('subject', 'predicate', 'object', 'context')]),
        ),
    ]
