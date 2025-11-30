from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    duration = models.CharField()

class Trainers(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()
    experience_years = models.IntegerField()

class Announcements(models.Model):
    title = models.CharField(max_length=20)
    message = models.TextField()
    date_posted = models.DateField()

    def __str__(self):
        return self.title