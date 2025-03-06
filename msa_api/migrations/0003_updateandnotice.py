# Generated by Django 5.1.4 on 2025-02-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msa_api', '0002_executivecommittee'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateAndNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to='updates_and_notices/')),
                ('date', models.DateField()),
            ],
        ),
    ]
