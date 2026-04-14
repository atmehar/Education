from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    address = models.CharField(' ' , max_length=150)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name