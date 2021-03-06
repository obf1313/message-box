# Generated by Django 2.1.5 on 2019-01-25 07:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190122_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3b3df886-179b-49c9-ace9-cd4dac9e5d0d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e8a5c814-2b41-4fce-9ee5-072fac992605'), editable=False, primary_key=True, serialize=False),
        ),
    ]
