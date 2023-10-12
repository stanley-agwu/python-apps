from rest_framework import viewsets
from rest_framework.response import Response

from school.models import Course, Student
from .serializer import CourseSerializer, StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data

        new_student = Student.objects.create(name=data['name'], age=data['age'], grade=data['grade'])
        new_student.save()

        for course in data['courses']:
            course_obj = Course.objects.get(title=course['title'])
            new_student.courses.add(course_obj)

        serializer = StudentSerializer(new_student)

        return Response(serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()