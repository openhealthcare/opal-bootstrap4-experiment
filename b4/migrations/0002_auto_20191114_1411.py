# Generated by Django 2.0.13 on 2019-11-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b4', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='symptomcomplex',
            options={'verbose_name': 'Symptom', 'verbose_name_plural': 'Symptom complexes'},
        ),
        migrations.AlterField(
            model_name='patientconsultation',
            name='when',
            field=models.DateField(blank=True, null=True),
        ),
    ]
