# Generated by Django 5.0a1 on 2023-11-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notey_app', '0011_rename_created_by_mood_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='mood_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
