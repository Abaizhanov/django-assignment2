from django.db import models
from students.models import Student
from courses.models import Course

class Attendance(models.Model):
    objects = None
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} - {'Present' if self.status else 'Absent'}"

# Create your models here.