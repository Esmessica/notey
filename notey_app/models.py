from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Note(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    # By default, it takes timezone from settings.py
    category = models.TextField
    title = models.CharField(max_length=225)
    text = RichTextField(blank=True, null=True)

    def publish(self):
        self.create_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('daily_advice')
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
        ('playful', 'playful'),
        ('bored', 'bored'),
        ('sick', 'sick'),
        ('sleepy', 'sleepy'),
        ('surprised', 'surprised'),
        ('unhappy', 'unhappy'),
        ('grumpy', 'grumpy')
    )
    my_mood = models.CharField(max_length=25, choices=MOOD_CHOICES)

    def __str__(self):
        return self.my_mood

class Advice(models.Model):
    mood_option = models.CharField(max_length=25, choices=Mood.MOOD_CHOICES)
    text_advice = models.TextField(max_length=600)

    def __str__(self):
        return f"Advice for {self.mood_option}"