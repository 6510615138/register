from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Subject(models.Model):
    subject_code = models.CharField(max_length=5)
    subject_name = models.CharField(max_length=64)
    host = models.CharField(max_length=64)
    seat = models.IntegerField()
    seat_max = models.IntegerField()
    gp = models.IntegerField()
    class_list = models.ManyToManyField(Student, blank=True, related_name="passengers")

    def __str__(self):
        return f"Subject: {self.subject_name} Host: ({self.host}) GP: ({self.gp}) Seat: ({self.seat})/({self.seat_max})"

class User(models.Model):
    id = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    email = models.EmailField()
    
    def __str__(self):
        return f"ID: ({self.id}) Name: ({self.name})"
        
    

class Student(models.Model.User):
    
    def __str__(self):
        return f"ID: ({self.id}) Name: ({self.name}) Role: Student"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    email = models.EmailField()
    
    def __str__(self):
        return f"ID: ({self.id}) Name: ({self.name}) Role: Teacher"





