# Generated by Django 3.2.23 on 2024-01-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_models_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='model',
            field=models.FileField(upload_to='model'),
        ),
    ]
