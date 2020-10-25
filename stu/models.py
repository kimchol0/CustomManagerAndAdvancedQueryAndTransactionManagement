from django.db import models


# Create your models here.
class Clazz(models.Model):
    cname = models.CharField(max_length=30)


class Student(models.Model):
    sname = models.CharField(max_length=30)
    score = models.PositiveIntegerField()
    cls = models.ForeignKey(Clazz,on_delete=models.CASCADE)
