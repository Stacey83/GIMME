# Generated by Django 3.2.5 on 2021-09-12 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='comments',
            field=models.CharField(default='', max_length=400),
        ),
    ]