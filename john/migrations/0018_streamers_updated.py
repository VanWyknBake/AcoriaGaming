# Generated by Django 3.1.7 on 2021-08-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0017_auto_20210804_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamers',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
