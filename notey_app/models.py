from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
# TODO make author for notes field that uses User model

class Note(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=225)
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('notey_app:all_notes')
    # redirects to daily advice based on mood

    def __str__(self):
        return self.title


class Mood(models.Model):
    mood_date = models.DateTimeField(default=timezone.now)
    MOOD_CHOICES = (
        ('angry', 'angry'),
        ('annoyed', 'annoyed'),
        ('sad', 'sad'),
        ('very sad', 'very sad'),
        ('fine', 'fine'),
        ('mischievous', 'mischievous'),
        ('excited', 'excited'),
        ('bored', 'bored'),
        ('sick', 'sick'),
        ('silly', 'silly'),
        ('sleepy', 'sleepy'),
        ('surprised', 'surprised'),
        ('unhappy', 'unhappy'),
        ('grumpy', 'grumpy')
    )
    my_mood = models.CharField(max_length=25, choices=MOOD_CHOICES)

    def __str__(self):
        return self.my_mood


class Advice(models.Model):

    MOOD_CHOICES = (
        ('angry', 'angry'),
        ('annoyed', 'annoyed'),
        ('sad', 'sad'),
        ('very sad', 'very sad'),
        ('fine', 'fine'),
        ('mischievous', 'mischievous'),
        ('excited', 'excited'),
        ('bored', 'bored'),
        ('sick', 'sick'),
        ('silly', 'silly'),
        ('sleepy', 'sleepy'),
        ('surprised', 'surprised'),
        ('unhappy', 'unhappy'),
        ('grumpy', 'grumpy')
    )
    mood_option = models.CharField(max_length=25, choices=MOOD_CHOICES)
    text_advice = models.TextField(max_length=600)

    def __str__(self):
        return f"Advice for {self.mood_option}"