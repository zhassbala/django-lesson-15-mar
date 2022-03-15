from django.urls import path
from . import views, rest_endpoints

urlpatterns = [
  path('', views.index, name='index'),
  path('students', views.students_list, name='students_list'),
  # path('students', views.get_students_list, name='get_students_list'),
  # path('students', rest_endpoints.get_students_list, name='get_students_list'),
]