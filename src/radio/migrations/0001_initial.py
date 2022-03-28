# Generated by Django 3.2.10 on 2022-03-12 00:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalAnnouncement',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('enabled', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalEmailTemplate',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('template_type', models.CharField(choices=[('welcome', 'welcome'), ('alert', 'alert')], max_length=30, unique=True)),
                ('enabled', models.BooleanField(default=False)),
                ('HTML', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScanList',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('public', models.BooleanField(default=False)),
                ('community_shared', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('enable_talkgroup_acls', models.BooleanField(default=False, verbose_name='Enable Talkgroup ACLs')),
                ('prune_transmissions', models.BooleanField(default=False, verbose_name='Enable Pruneing Transmissions')),
                ('prune_transmissions_after_days', models.IntegerField(default=365, verbose_name='Days to keep Transmissions (Prune)')),
            ],
        ),
        migrations.CreateModel(
            name='SystemRecorder',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('site_id', models.CharField(blank=True, max_length=100, null=True)),
                ('enabled', models.BooleanField(default=False)),
                ('api_key', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
            ],
        ),
        migrations.CreateModel(
            name='TalkGroup',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('decimal_id', models.IntegerField(db_index=True)),
                ('alpha_tag', models.CharField(blank=True, default='', max_length=30)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('mode', models.CharField(choices=[('digital', 'Digital'), ('analog', 'Analog'), ('tdma', 'TDMA'), ('mixed', 'Mixed')], default='digital', max_length=250)),
                ('encrypted', models.BooleanField(blank=True, default=False)),
                ('agency', models.ManyToManyField(blank=True, to='radio.Agency')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionFreq',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('time', models.DateTimeField()),
                ('freq', models.IntegerField(db_index=True, default=0)),
                ('pos', models.IntegerField(default=0)),
                ('len', models.IntegerField(default=0)),
                ('error_count', models.IntegerField(default=0)),
                ('spike_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('decimal_id', models.IntegerField(db_index=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('site_admin', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('site_theme', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAlert',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('enabled', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('web_notification', models.BooleanField(default=False)),
                ('app_rise_notification', models.BooleanField(default=False)),
                ('app_rise_urls', models.TextField(default='', verbose_name=', Seperated AppriseURL(s)')),
                ('emergencyOnly', models.BooleanField(default=False)),
                ('title', models.CharField(default='New Activity Alert', max_length=255)),
                ('body', models.TextField(default='New Activity on %T - %I')),
                ('talkgroups', models.ManyToManyField(blank=True, to='radio.TalkGroup')),
                ('units', models.ManyToManyField(blank=True, to='radio.Unit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='radio.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionUnit',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('time', models.DateTimeField(db_index=True)),
                ('pos', models.IntegerField(default=0)),
                ('emergency', models.BooleanField(default=0)),
                ('signal_system', models.CharField(blank=True, default='', max_length=50)),
                ('tag', models.CharField(blank=True, default='', max_length=255)),
                ('length', models.FloatField(default=0.0)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('audio_file', models.FileField(upload_to='audio/%Y/%m/%d/')),
                ('encrypted', models.BooleanField(db_index=True, default=False)),
                ('emergency', models.BooleanField(db_index=True, default=False)),
                ('frequency', models.FloatField(default=0.0)),
                ('length', models.FloatField(default=0.0, null=True)),
                ('locked', models.BooleanField(db_index=True, default=False)),
                ('transcript', models.TextField(blank=True, null=True)),
                ('frequencys', models.ManyToManyField(blank=True, to='radio.TransmissionFreq')),
                ('recorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.systemrecorder')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
                ('talkgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.talkgroup')),
                ('units', models.ManyToManyField(blank=True, to='radio.TransmissionUnit')),
            ],
            options={
                'ordering': ['-start_time'],
            },
        ),
        migrations.CreateModel(
            name='TalkGroupACL',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('default_new_users', models.BooleanField(default=True)),
                ('download_allowed', models.BooleanField(default=True)),
                ('allowed_talkgroups', models.ManyToManyField(to='radio.TalkGroup')),
                ('users', models.ManyToManyField(to='radio.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='systemrecorder',
            name='talkgroups_allowed',
            field=models.ManyToManyField(blank=True, related_name='SRTGAllow', to='radio.TalkGroup'),
        ),
        migrations.AddField(
            model_name='systemrecorder',
            name='talkgroups_denyed',
            field=models.ManyToManyField(blank=True, related_name='SRTGDeny', to='radio.TalkGroup'),
        ),
        migrations.AddField(
            model_name='systemrecorder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='radio.userprofile'),
        ),
        migrations.CreateModel(
            name='SystemForwarder',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('enabled', models.BooleanField(default=False)),
                ('recorder_key', models.UUIDField()),
                ('remote_url', models.CharField(max_length=250)),
                ('forward_incidents', models.BooleanField(default=False)),
                ('forwarded_systems', models.ManyToManyField(to='radio.System')),
                ('talkgroup_filter', models.ManyToManyField(blank=True, to='radio.TalkGroup')),
            ],
        ),
        migrations.CreateModel(
            name='SystemACL',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('public', models.BooleanField(default=False)),
                ('users', models.ManyToManyField(blank=True, to='radio.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='system',
            name='systemACL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.systemacl'),
        ),
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('public', models.BooleanField(default=True)),
                ('community_shared', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.userprofile')),
                ('scanlists', models.ManyToManyField(to='radio.ScanList')),
            ],
        ),
        migrations.AddField(
            model_name='scanlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.userprofile'),
        ),
        migrations.AddField(
            model_name='scanlist',
            name='talkgroups',
            field=models.ManyToManyField(to='radio.TalkGroup'),
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('agency', models.ManyToManyField(blank=True, to='radio.Agency')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
                ('transmission', models.ManyToManyField(blank=True, to='radio.Transmission')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.AddField(
            model_name='agency',
            name='city',
            field=models.ManyToManyField(blank=True, to='radio.City'),
        ),
    ]