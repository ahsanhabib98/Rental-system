# Generated by Django 2.0.5 on 2018-12-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproperty',
            name='detail',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]
