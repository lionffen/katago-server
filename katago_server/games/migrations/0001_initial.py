# Generated by Django 2.2.8 on 2019-12-24 17:51

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trainings', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_size', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=19), size=2)),
                ('handicap', models.IntegerField(default=0)),
                ('komi', models.DecimalField(decimal_places=1, default=7.0, max_digits=3)),
                ('ko_rule', models.CharField(choices=[('Simple', 'SIMPLE'), ('Positional', 'POSITIONAL'), ('Situational', 'SITUATIONAL')], max_length=15)),
                ('scoring_rule', models.CharField(choices=[('Area', 'AREA'), ('Territory', 'TERRITORY')], max_length=15)),
                ('tax_rule', models.CharField(choices=[('None', 'NONE'), ('Seki', 'SEKI'), ('All', 'ALL')], max_length=15)),
                ('multi_stone_suicide_allowed', models.BooleanField()),
                ('extra_rules', django.contrib.postgres.fields.jsonb.JSONField()),
                ('result', models.CharField(choices=[('W', 'WHITE'), ('B', 'BLACK'), ('0', 'JIGO'), ('∅', 'MOSHOUBOU')], max_length=15)),
                ('has_resigned', models.BooleanField()),
                ('score', models.DecimalField(decimal_places=1, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sgf_file', models.FileField(upload_to='')),
                ('unpacked_training_file', models.FileField(upload_to='')),
                ('packed_training_file', models.FileField(upload_to='')),
                ('game_extra_params', django.contrib.postgres.fields.jsonb.JSONField()),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trainings.Network')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_size', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=19), size=2)),
                ('handicap', models.IntegerField(default=0)),
                ('komi', models.DecimalField(decimal_places=1, default=7.0, max_digits=3)),
                ('ko_rule', models.CharField(choices=[('Simple', 'SIMPLE'), ('Positional', 'POSITIONAL'), ('Situational', 'SITUATIONAL')], max_length=15)),
                ('scoring_rule', models.CharField(choices=[('Area', 'AREA'), ('Territory', 'TERRITORY')], max_length=15)),
                ('tax_rule', models.CharField(choices=[('None', 'NONE'), ('Seki', 'SEKI'), ('All', 'ALL')], max_length=15)),
                ('multi_stone_suicide_allowed', models.BooleanField()),
                ('extra_rules', django.contrib.postgres.fields.jsonb.JSONField()),
                ('result', models.CharField(choices=[('W', 'WHITE'), ('B', 'BLACK'), ('0', 'JIGO'), ('∅', 'MOSHOUBOU')], max_length=15)),
                ('has_resigned', models.BooleanField()),
                ('score', models.DecimalField(decimal_places=1, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sgf_file', models.FileField(upload_to='')),
                ('gating', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trainings.Gating')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='ForkedSelfPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_size', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=19), size=2)),
                ('handicap', models.IntegerField(default=0)),
                ('komi', models.DecimalField(decimal_places=1, default=7.0, max_digits=3)),
                ('ko_rule', models.CharField(choices=[('Simple', 'SIMPLE'), ('Positional', 'POSITIONAL'), ('Situational', 'SITUATIONAL')], max_length=15)),
                ('scoring_rule', models.CharField(choices=[('Area', 'AREA'), ('Territory', 'TERRITORY')], max_length=15)),
                ('tax_rule', models.CharField(choices=[('None', 'NONE'), ('Seki', 'SEKI'), ('All', 'ALL')], max_length=15)),
                ('multi_stone_suicide_allowed', models.BooleanField()),
                ('extra_rules', django.contrib.postgres.fields.jsonb.JSONField()),
                ('result', models.CharField(choices=[('W', 'WHITE'), ('B', 'BLACK'), ('0', 'JIGO'), ('∅', 'MOSHOUBOU')], max_length=15)),
                ('has_resigned', models.BooleanField()),
                ('score', models.DecimalField(decimal_places=1, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sgf_file', models.FileField(upload_to='')),
                ('unpacked_training_file', models.FileField(upload_to='')),
                ('packed_training_file', models.FileField(upload_to='')),
                ('parent_sgf_file', models.FileField(upload_to='')),
                ('forked_at_turn', models.IntegerField()),
                ('game_extra_params', django.contrib.postgres.fields.jsonb.JSONField()),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trainings.Network')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
