# Generated by Django 2.2.2 on 2019-06-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unburden',
            old_name='dateNow',
            new_name='date_now',
        ),
        migrations.RenameField(
            model_name='unburden',
            old_name='dateOccurrence',
            new_name='date_unburden',
        ),
        migrations.AddField(
            model_name='unburden',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='unburden',
            name='follow',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='unburden',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]