# Generated by Django 3.1.2 on 2021-02-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0003_auto_20210218_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DateOfBirth',
            field=models.DateField(max_length=150),
        ),
    ]
