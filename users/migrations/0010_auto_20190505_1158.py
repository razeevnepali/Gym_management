# Generated by Django 2.1.5 on 2019-05-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190414_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media\\default.jpg', upload_to='profile_pics'),
        ),
    ]