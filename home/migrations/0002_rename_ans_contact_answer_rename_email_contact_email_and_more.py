# Generated by Django 4.0.3 on 2022-03-18 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='ans',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
    ]
