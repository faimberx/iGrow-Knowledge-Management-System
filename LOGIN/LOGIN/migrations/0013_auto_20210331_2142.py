# Generated by Django 3.1.2 on 2021-03-31 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0012_auto_20210331_2140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Discussion',
            new_name='Group',
        ),
        migrations.AlterModelTable(
            name='booking',
            table='Booking',
        ),
        migrations.AlterModelTable(
            name='group',
            table='Group',
        ),
    ]