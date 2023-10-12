from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    class_room = models.IntegerField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    courses = models.ManyToManyField(Course, related_name="students")

    def __str__(self):
        return self.name