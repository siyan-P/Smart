# Generated by Django 4.1.7 on 2023-03-16 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listMed_app', '0007_alter_medmodel_afterfood_alter_medmodel_beforefood'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medmodel',
            old_name='afterFood',
            new_name='medicineTime',
        ),
    ]
