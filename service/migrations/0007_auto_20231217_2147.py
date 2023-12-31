# Generated by Django 3.2.23 on 2023-12-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_alter_models_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='model',
            field=models.FileField(blank=True, null=True, upload_to='models/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/'),
        ),
    ]
