# Generated by Django 3.1.7 on 2021-04-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_job_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='Job Title', max_length=50),
        ),
    ]
