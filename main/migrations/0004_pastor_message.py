# Generated by Django 5.0.6 on 2024-05-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastor',
            name='message',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
