# Generated by Django 2.2.1 on 2019-10-01 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0004_auto_20191001_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='date',
            field=models.CharField(max_length=36),
        ),
    ]
