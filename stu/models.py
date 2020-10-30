from django.db import models
from django.db.transaction import atomic


# Create your models here.
class Clazz(models.Model):
    cname = models.CharField(max_length=30)


class Student(models.Model):
    sname = models.CharField(max_length=30)
    score = models.PositiveIntegerField()
    cls = models.ForeignKey(Clazz, on_delete=models.CASCADE)

    def __str__(self):
        return u'Student:%s,%s' % (self.sname, self.score)

    @atomic
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.cls = Clazz.objects.get(cname=self.cls.cname)
        except:
            self.cls = Clazz.objects.create(cname=self.cls.cname)

        1/0
        '''
        >>>from stu.models import *
        >>>stu = Student(sname='xiena',score=30,cls=Clazz(cname='AI'))
        >>>stu.save()
        Traceback (most recent call last):
          File "<input>", line 1, in <module>
          File "C:\Program Files\Python38\lib\contextlib.py", line 75, in inner
            return func(*args, **kwds)
          File "D:\workspace\Pycharm\CustomManagerAndAdvancedQueryAndTransactionManagement\stu\models.py", line 26, in save
            1/0
        ZeroDivisionError: division by zero

        '''

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
