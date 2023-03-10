# Generated by Django 4.1.7 on 2023-03-08 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listMed_app', '0002_alter_medmodel_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medmodel',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medmodel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MedModel', to=settings.AUTH_USER_MODEL),
        ),
    ]
