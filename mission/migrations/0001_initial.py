# Generated by Django 3.2 on 2021-04-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_personnel', models.FloatField()),
                ('objet', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('pays', models.CharField(max_length=200, null=True)),
                ('ville', models.CharField(max_length=200, null=True)),
                ('ordre', models.FileField(upload_to='')),
                ('debut', models.DateField()),
                ('fin', models.DateField()),
            ],
            options={
                'db_table': 'mission',
            },
        ),
        migrations.CreateModel(
            name='RapportMissionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mission', models.FloatField()),
                ('rapport', models.FileField(upload_to='')),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'rapportmission',
            },
        ),
    ]
