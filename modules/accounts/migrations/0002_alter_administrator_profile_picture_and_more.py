# Generated by Django 4.0.1 on 2022-07-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='profile', verbose_name='profile picture'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='profile', verbose_name='profile picture'),
        ),
    ]
