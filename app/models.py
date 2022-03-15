from django.db import models

class Adviser(models.Model):
  firstname = models.CharField(max_length=200)
  lastname = models.CharField(max_length=200)
  
  def __str__(self):
    return self.firstname + ' ' + self.lastname

class Course(models.Model):
  course_code = models.CharField(max_length=7)
  
  def __str__(self):
    return self.course_code


class Student(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  
  courses = models.ManyToManyField(to=Course, related_name='students', null=True, blank=True)
  adviser = models.ForeignKey(to=Adviser, related_name='students', 
                              on_delete=models.SET_NULL, 
                              blank=True, null=True)
  def __str__(self):
    return self.firstname + ' ' + self.lastname 
  

