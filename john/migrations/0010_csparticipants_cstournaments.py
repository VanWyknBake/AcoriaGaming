# Generated by Django 3.1.7 on 2021-08-02 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0009_armaparticipants_armatournaments'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSTournaments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='tournaments/')),
                ('tournament_type', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('when', models.DateTimeField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='john.games')),
            ],
            options={
                'verbose_name': 'CSGO Participant',
                'verbose_name_plural': 'CSGO Participants',
            },
        ),
        migrations.CreateModel(
            name='CSParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=20)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='john.cstournaments')),
            ],
        ),
    ]
