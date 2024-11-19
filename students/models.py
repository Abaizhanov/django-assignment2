from django.db import models
from users.models import CustomUser


class Student(models.Model):
    objects = None
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    dob = models.DateField()
    registration_date = models.DateField(auto_now_add=True)
