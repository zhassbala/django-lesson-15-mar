from django.shortcuts import render
from .models import Student

def index(request):
  return render(request, "index.html", {'a': [23, 12, 4, 45, 567, 1, 4]})


def students_list(request):
  students = Student.objects.all()
  return render(request, 'students_list.html', {'students': students})

def get_students_list(request):
  students = Student.objects.all()
  return students