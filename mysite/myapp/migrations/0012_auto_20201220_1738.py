# Generated by Django 3.1.4 on 2020-12-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_script_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='myapp/static/img', verbose_name='Image'),
        ),
    ]
