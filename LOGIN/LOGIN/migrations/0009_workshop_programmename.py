# Generated by Django 3.1.2 on 2021-02-25 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0008_auto_20210224_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='ProgrammeName',
            field=models.CharField(default='', max_length=150),
        ),
    ]