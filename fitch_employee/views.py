import imp
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from datetime import datetime
from create_employee.models import Employee

# Create your views here.
def retrive(request):
    data = Employee.objects.all()
    return render(request,"index.html",{"employeedata":data})
    
