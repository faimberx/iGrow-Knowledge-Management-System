# Generated by Django 3.1.2 on 2021-02-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0004_auto_20210220_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DateOfBirth',
            field=models.CharField(max_length=150),
        ),
    ]