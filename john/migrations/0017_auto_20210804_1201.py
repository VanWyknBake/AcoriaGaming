# Generated by Django 3.1.7 on 2021-08-04 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0016_profile2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile2',
            old_name='about',
            new_name='streamers',
        ),
    ]