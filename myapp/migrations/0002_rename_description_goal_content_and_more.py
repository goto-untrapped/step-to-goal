# Generated by Django 5.0.3 on 2024-03-20 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='subject',
            new_name='name',
        ),
    ]
