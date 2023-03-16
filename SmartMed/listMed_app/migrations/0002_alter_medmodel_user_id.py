# Generated by Django 4.1.7 on 2023-03-08 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listMed_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medmodel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='MedModel', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]