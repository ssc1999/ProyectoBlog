# Generated by Django 3.1.3 on 2020-12-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_category_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='user',
            field=models.CharField(default='Serch', max_length=20),
        ),
    ]
