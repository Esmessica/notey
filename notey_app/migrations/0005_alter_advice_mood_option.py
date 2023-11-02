# Generated by Django 5.0a1 on 2023-10-28 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notey_app', '0004_remove_advice_my_mood_advice_mood_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='mood_option',
            field=models.CharField(choices=[('angry', 'angry'), ('annoyed', 'annoyed'), ('sad', 'sad'), ('very sad', 'very sad'), ('fine', 'fine'), ('mischievous', 'mischievous'), ('excited', 'excited'), ('playful', 'playful'), ('bored', 'bored'), ('sick', 'sick'), ('silly', 'silly'), ('sleepy', 'sleepy'), ('surprised', 'surprised'), ('unhappy', 'unhappy'), ('grumpy', 'grumpy')], max_length=25),
        ),
    ]
