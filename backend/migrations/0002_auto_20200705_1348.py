# Generated by Django 3.0.8 on 2020-07-05 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='created',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='log',
            name='created_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
