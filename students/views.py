from django.shortcuts import render
from .models import Student
from rest_framework.viewsets import ModelViewSet
from students.serializers import StudentModelSerializer
from rest_framework import permissions
from students.permissions import IsOwnerOrReadOnly


def student(request):
    students = Student.objects.all()
    return render(request, "all_student.html", {"students": students})


def details(request, id):
    student = Student.objects.get(id=id)
    return render(request, "details.html", {"student": student})


def main(request):
    students = Student.objects.all()
    return render(request, "main.html", {"students": students})


def upload(request):
    if request.method == "POST":
        file = request.FILES["image"]
        student = Student.objects.create(image=file)

    return render(request, "upload.html", {"student": student})


def dashboard(request):
    return render(request, "dashboard.html")


def home(request):
    return render(request, "home.html")


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
