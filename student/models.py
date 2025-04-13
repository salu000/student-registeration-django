from django.db import models

class Student(models.Model):
    CLASS_CHOICES = [
        ('Morning A', 'Morning A'),
        ('Morning B', 'Morning B'),
        ('Morning C', 'Morning C'),
    ]
    roll_no = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    std_class = models.CharField(max_length=20, choices=CLASS_CHOICES, default='Morning B')

    def __str__(self):
        return self.name
