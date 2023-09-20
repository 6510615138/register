from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Personnel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return f"ID: ({self.id}) Name: ({self.name})"

class Student(Personnel):
    role = models.CharField(max_length=20, default="Student")  # Add a role field
    # You can add more student-specific fields here

    def __str__(self):
        return f"ID: ({self.id}) Name: ({self.name}) Role: {self.role}"

class Teacher(Personnel):
    role = models.CharField(max_length=20, default="Teacher")  # Add a role field
    # You can add more teacher-specific fields here

    def __str__(self):
        return f"ID: ({self.id}) Name: ({self.name}) Role: {self.role}"

class Subject(models.Model):
    code = models.CharField(max_length=5)
    title = models.CharField(max_length=64)
    host = models.ManyToManyField(Teacher, blank=True, related_name="taught_subjects")
    seat = models.IntegerField()
    seat_max = models.IntegerField()
    gp = models.IntegerField()
    class_list = models.ManyToManyField(Student, blank=True, related_name="enrolled_subjects")

    def __str__(self):
        return f"Subject: {self.title} GP: ({self.gp}) Seat: ({self.seat})/({self.seat_max})"
