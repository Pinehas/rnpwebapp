# Generated by Django 3.2 on 2021-04-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cmd_Prod_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_client', models.IntegerField()),
                ('id_produit', models.IntegerField()),
                ('quantite', models.IntegerField()),
                ('details', models.CharField(max_length=2000)),
                ('piece_cmd', models.FileField(upload_to='')),
                ('statut', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cmdproduit',
            },
        ),
        migrations.CreateModel(
            name='Dmd_Serv_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_client', models.IntegerField()),
                ('id_service', models.IntegerField()),
                ('details', models.CharField(max_length=2000)),
                ('piece_dmd', models.FileField(upload_to='')),
                ('statut', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'dmdservice',
            },
        ),
    ]