# Generated by Django 5.0.3 on 2024-03-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_testtodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtarget',
            name='target_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testtodo',
            name='todo_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]