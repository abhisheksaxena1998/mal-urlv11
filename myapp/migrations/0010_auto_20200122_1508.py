# Generated by Django 2.2.7 on 2020-01-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200122_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='rank',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
