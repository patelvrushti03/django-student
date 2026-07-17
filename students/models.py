from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    course = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return self.name
