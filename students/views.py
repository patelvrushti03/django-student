from django.shortcuts import render
from .models import Student

def student(request):
    students = Student.objects.all()
    return render(request, "all_student.html",{'students':students})

def details(request, id):
    student = Student.objects.get(id=id)
    return render(request, "details.html", {'student': student})

def main(request):
    students = Student.objects.all()
    return render(request, "main.html",{'students':students})

def upload(request):
    if request.method == "POST":
        file = request.FILES['image']
        student = Student.objects.create(image=file)
        
    return render(request,'upload.html',{'student':student})