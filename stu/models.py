from django.db import models


# Create your models here.
class Clazz(models.Model):
    cname = models.CharField(max_length=30)


class Student(models.Model):
    sname = models.CharField(max_length=30)
    score = models.PositiveIntegerField()
    cls = models.ForeignKey(Clazz, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.cls = Clazz.objects.get(cname=self.cls.cname)
        except:
            self.cls = Clazz.objects.create(cname=self.cls.cname)
        # 学生表的插入
        models.Model.save(self, force_insert=False, force_update=False, using=None,
                          update_fields=None)


'''
控制台输入
>>>from stu.models import *
>>>stus = Student(sname='zhangsan',score=88,cls=Clazz(cname='B201Python班'))
>>>stus.save()
即可执行save方法
'''
