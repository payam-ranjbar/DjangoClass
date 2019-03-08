from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 50)
    studId = models.CharField(max_length = 20)

class Dorm(models.Model):
    name = models.CharField(max_length = 50)
    students = models.ManyToManyField(Student)
