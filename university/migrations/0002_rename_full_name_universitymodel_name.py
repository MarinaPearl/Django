# Generated by Django 4.2.7 on 2023-11-28 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='universitymodel',
            old_name='full_name',
            new_name='name',
        ),
    ]
