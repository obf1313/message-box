# Generated by Django 2.1.5 on 2019-01-30 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190130_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default='6c2b20df-ddc3-4801-93b5-78941c3cee8f', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default='8055245d-6248-41a9-95b7-3dbc979e5032', editable=False, primary_key=True, serialize=False),
        ),
    ]
