# Generated by Django 3.2 on 2021-04-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_personnel', models.IntegerField()),
                ('service', models.CharField(max_length=200)),
                ('poste', models.CharField(max_length=200)),
                ('motif', models.CharField(max_length=200)),
                ('piece_justif', models.FileField(upload_to='')),
                ('duree', models.IntegerField()),
            ],
            options={
                'db_table': 'permission',
            },
        ),
    ]