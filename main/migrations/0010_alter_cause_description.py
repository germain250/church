# Generated by Django 5.0.6 on 2024-05-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_event_pastor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
