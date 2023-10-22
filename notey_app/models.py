from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Note(models.Model):
    create_date = models.DateTimeField(default=timezone.now)
    # By default, it takes timezone from settings.py
    title = models.CharField(max_length=225)
    text = RichTextField(blank=True, null=True)

    def publish(self):
        self.create_date = timezone.now()
        self.save()
