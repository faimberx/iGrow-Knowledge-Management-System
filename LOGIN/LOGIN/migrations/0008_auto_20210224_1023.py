# Generated by Django 3.1.2 on 2021-02-24 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0007_auto_20210220_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='Title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='feed',
            name='Video',
            field=models.FileField(null=True, upload_to='uploads/', verbose_name=''),
        ),
    ]
