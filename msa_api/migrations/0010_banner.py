# Generated by Django 5.1.4 on 2025-03-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msa_api', '0009_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]
