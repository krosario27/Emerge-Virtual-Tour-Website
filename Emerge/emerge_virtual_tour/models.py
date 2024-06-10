from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    pathway = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/')
    project_poster = models.ImageField(upload_to='project_posters/')
    bio = models.TextField()

    def __str__(self):
        return self.full_name
