# Generated by Django 4.1.4 on 2023-01-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='songpopularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Highest_Charting_Position', models.IntegerField()),
                ('Number_of_Times_Charted', models.IntegerField()),
                ('Artist_Followers', models.IntegerField()),
                ('Genre', models.IntegerField()),
                ('Danceability', models.IntegerField()),
                ('Energy', models.IntegerField()),
                ('Loudness', models.IntegerField()),
                ('Valence', models.IntegerField()),
                ('Duration', models.IntegerField()),
                ('Tempo', models.IntegerField()),
                ('Liveness', models.IntegerField()),
                ('Acousticness', models.IntegerField()),
                ('Speechiness', models.IntegerField()),
            ],
        ),
    ]
