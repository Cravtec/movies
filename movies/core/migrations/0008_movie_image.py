# Generated by Django 3.1.2 on 2020-11-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201029_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='movie_cover'),
        ),
    ]
