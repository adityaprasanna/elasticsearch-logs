# Generated by Django 3.0.2 on 2020-01-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearch_logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='threshold',
            field=models.CharField(default='NA', max_length=20),
        ),
    ]
