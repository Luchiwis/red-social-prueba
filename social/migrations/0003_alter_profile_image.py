# Generated by Django 4.1.2 on 2022-10-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='./static/batman.png', upload_to='profile_pics'),
        ),
    ]