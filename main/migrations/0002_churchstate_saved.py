# Generated by Django 5.0.6 on 2024-05-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='churchstate',
            name='saved',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
