# Generated by Django 2.0.5 on 2018-12-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_addproperty_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproperty',
            name='photo',
            field=models.ImageField(blank=True, upload_to='property_image'),
        ),
    ]