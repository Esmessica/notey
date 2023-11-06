# Generated by Django 5.0a1 on 2023-11-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notey_app', '0006_alter_mood_my_mood'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.TextField(blank=True, max_length='120', null=True),
        ),
        migrations.AlterField(
            model_name='advice',
            name='mood_option',
            field=models.CharField(choices=[('angry', 'angry'), ('annoyed', 'annoyed'), ('sad', 'sad'), ('very sad', 'very sad'), ('fine', 'fine'), ('mischievous', 'mischievous'), ('excited', 'excited'), ('bored', 'bored'), ('sick', 'sick'), ('silly', 'silly'), ('sleepy', 'sleepy'), ('surprised', 'surprised'), ('unhappy', 'unhappy'), ('grumpy', 'grumpy')], max_length=25),
        ),
        migrations.AlterField(
            model_name='mood',
            name='my_mood',
            field=models.CharField(choices=[('angry', 'angry'), ('annoyed', 'annoyed'), ('sad', 'sad'), ('very sad', 'very sad'), ('fine', 'fine'), ('mischievous', 'mischievous'), ('excited', 'excited'), ('bored', 'bored'), ('sick', 'sick'), ('silly', 'silly'), ('sleepy', 'sleepy'), ('surprised', 'surprised'), ('unhappy', 'unhappy'), ('grumpy', 'grumpy')], max_length=25),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]