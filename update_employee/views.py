import imp
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from datetime import datetime
from create_employee.models import Employee
from django.contrib import messages

# Create your views here.
def update(request,id):
    employee_details = Employee.objects.get(id = id)
    return render(request,"edit.html",{"employeedata":employee_details})

def update_employee(request):
    now = datetime.now()
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dept = request.POST.get('dept')
        
        update = Employee.objects.get(email = email)
        
        
        
        if(update):
            update.name = name
            update.mobile = mobile
            update.dept = dept
            update.email = email
            update.lastmodified_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
            update.save()
            
            messages.success(request, "Employee Updated Sucessfully.")
            return render(request,"index.html")
        else:
            return render(request,"index.html")
    else:
        return render(request,"index.html")
    
