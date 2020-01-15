# Generated by Django 3.0.2 on 2020-01-15 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Webinterface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testrailcaseid', models.CharField(blank=True, max_length=12, null=True)),
                ('descr', models.CharField(max_length=255, verbose_name='Title')),
                ('isenabled', models.BooleanField(default=True)),
                ('url', models.CharField(blank=True, max_length=1024)),
                ('method', models.CharField(blank=True, choices=[('POST', 'post'), ('GET', 'get'), ('OPTIONS', 'options'), ('HEAD', 'head'), ('PUT', 'put'), ('PATCH', 'patch'), ('DELETE', 'delete')], max_length=12)),
                ('headers', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('cookies', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('data', models.TextField(blank=True, default=None, null=True)),
                ('files', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('auth', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('timeout', models.CharField(blank=True, default=None, max_length=8, null=True)),
                ('allow_redirects', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('proxies', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('verify', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('stream', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('cert', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('debuginfo', models.TextField(blank=True, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
                ('moduleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Module')),
                ('projectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Webresponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('params', models.TextField(blank=True, null=True)),
                ('exectime', models.CharField(blank=True, max_length=16)),
                ('expected', models.CharField(blank=True, max_length=255, null=True)),
                ('actual', models.CharField(blank=True, max_length=255, null=True)),
                ('status_code', models.CharField(blank=True, max_length=4)),
                ('Response_content', models.TextField(blank=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
                ('webinterfaceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webinterface.Webinterface')),
            ],
        ),
    ]
