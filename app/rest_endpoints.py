from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_students_list(request):
  students = Student.objects.all()
  serializer = StudentSerializer(students, many=True)
  return Response(serializer.data)
