from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Personnel(User):
    def __str__(self):
        return f"ID: ({self.id}) Name: {self.first_name} {self.last_name}"
        
class Teacher(Personnel):
    role = "teacher"
    def __str__(self):
        return f"ID: ({self.id}) Name: ({self.name})"
    
    def getName():
        return self.first_name

class Student(Personnel):
    role = "student"
    advisor = models.ForeignKey(Teacher, related_name='Teacher', on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name


class Subject(models.Model):
    subject_code = models.CharField(max_length=5)
    subject_name = models.CharField(max_length=64)
    host = models.ManyToManyField(Teacher)
    seat_max = models.IntegerField()
    seat= models.IntegerField()
    gp = models.IntegerField()
    class_list = models.ManyToManyField(Personnel, blank=True,)

    def __str__(self):
        return f"{self.subject_code} {self.subject_name} GP: ({self.gp}) Seat: ({self.seat})/({self.seat_max})"




