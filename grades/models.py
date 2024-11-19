from django.db import models
from students.models import Student
from courses.models import Course
from users.models import CustomUser

class Grade(models.Model):
    objects = None
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)
    date = models.DateField(auto_now=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name}: {self.grade}"

# Create your models here.
