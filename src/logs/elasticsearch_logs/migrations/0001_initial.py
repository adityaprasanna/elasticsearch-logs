# Generated by Django 3.0.2 on 2020-01-06 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('client_id', models.CharField(max_length=100)),
                ('query_id', models.CharField(max_length=100)),
                ('question', models.TextField()),
                ('question_matched', models.TextField()),
                ('answer', models.TextField()),
                ('score', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
