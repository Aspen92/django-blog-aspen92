# Generated by Django 3.2.16 on 2022-12-08 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='lkes',
            new_name='likes',
        ),
    ]
