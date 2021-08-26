# Generated by Django 3.1.2 on 2021-01-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=255)),
                ('Pictures', models.ImageField(upload_to='uploads/')),
                ('Video', models.FileField(upload_to='uploads/')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About', models.CharField(max_length=1000)),
                ('Discussion', models.CharField(max_length=1000)),
                ('Media', models.FileField(upload_to='uploads/')),
                ('Member', models.CharField(max_length=150)),
                ('Name', models.CharField(max_length=150)),
                ('ProfilePictures', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'db_table': 'Discussion',
            },
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pictures', models.ImageField(upload_to='uploads/')),
                ('Species', models.CharField(max_length=150)),
                ('Types', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Plants',
            },
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Detail', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'SensorData',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Date', models.DateField()),
                ('Session', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Workshop',
            },
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='graph',
            new_name='Graph',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='description',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='photo',
            new_name='Photo',
        ),
        migrations.RenameField(
            model_name='feed',
            old_name='video',
            new_name='Video',
        ),
        migrations.AlterModelTable(
            name='feed',
            table='Feed',
        ),
    ]
