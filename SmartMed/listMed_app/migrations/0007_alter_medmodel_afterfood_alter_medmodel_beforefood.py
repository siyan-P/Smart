# Generated by Django 4.1.7 on 2023-03-16 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listMed_app', '0006_alter_medmodel_afterfood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medmodel',
            name='afterFood',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='medmodel',
            name='beforeFood',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
