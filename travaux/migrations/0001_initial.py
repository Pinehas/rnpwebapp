# Generated by Django 3.2 on 2021-04-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=200)),
                ('client', models.CharField(max_length=200)),
                ('categorie', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
                ('quartier', models.CharField(max_length=200)),
                ('duree', models.IntegerField()),
                ('contrat_projet', models.FileField(upload_to='')),
                ('tdr_projet', models.FileField(upload_to='')),
                ('cahier_projet', models.FileField(upload_to='')),
                ('date_contrat', models.DateField()),
                ('date_debut', models.DateField()),
                ('montant', models.FloatField()),
                ('details', models.TextField()),
                ('statut', models.CharField(max_length=200, null=True)),
                ('date_lancement', models.DateField(null=True)),
                ('date_fin', models.DateField(null=True)),
            ],
        ),
    ]