import imp
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from datetime import datetime
from create_employee.models import Employee
# Create your views here.
def delete(request,id):
    employee_details = Employee.objects.get(id = id).delete()
    return render(request,"edit.html")
