from django.shortcuts import render
from .models import Dorm, Student

# Create your views here.

def DormResidents(request, DormName):
    dorm = Dorm.objects.get(name = DormName)

    context = {
        "DormName" : DormName,
        "students": dorm.students.all
    }


    return render(request, 'StudAndDorm/index.html', context=context)

