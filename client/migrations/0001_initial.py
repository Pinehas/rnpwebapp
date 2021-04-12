# Generated by Django 3.2 on 2021-04-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('categorie', models.CharField(max_length=200)),
                ('telephone', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('pays', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
                ('quartier', models.CharField(max_length=200)),
                ('img_client', models.FileField(upload_to='')),
                ('password', models.CharField(max_length=200)),
                ('date_inscription', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='MessageClientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_client', models.IntegerField()),
                ('message', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('piece_client', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'messageclient',
            },
        ),
        migrations.CreateModel(
            name='ReponseClientModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_client', models.IntegerField()),
                ('message', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('piece_service', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'reponseclient',
            },
        ),
    ]