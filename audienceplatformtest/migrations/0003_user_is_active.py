# Generated by Django 3.2 on 2023-10-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audienceplatformtest', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]