from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'index.html')

def virtual_tour_landing(request):
    return render(request, 'virtual_tour_landing.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def vr_sroom(request):
    return render(request, 'vr_sroom.html')

def vr_xblock(request):
    return render(request, 'vr_xblock.html')
