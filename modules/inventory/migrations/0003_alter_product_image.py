# Generated by Django 4.0.1 on 2022-07-11 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_category_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='prod1.png', upload_to='products/', verbose_name='image'),
        ),
    ]