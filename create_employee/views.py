import imp
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from datetime import datetime
from create_employee.models import Employee
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.
# def create(request):
#     now = datetime.now()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         mobile = request.POST.get('mobile')
#         dept = request.POST.get('dept')
        
#         employee = Employee()
#         employee.name = name
#         employee.mobile = mobile
#         employee.dept = dept
#         employee.email = email
#         employee.created_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
#         employee.lastmodified_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
#         employee.save()
        
#         messages.success(request, "The Employee "+ name +"Inserted Sucessfully")
#         return render(request,"create.html")
#     else:
#         return render(request,"create.html")

@csrf_exempt
def create(request):
    now = datetime.now()
    if request.method == 'POST':
        recived_json_data = json.loads(request.body)
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # mobile = request.POST.get('mobile')
        # dept = request.POST.get('dept')
        name = recived_json_data['name']
        email = recived_json_data['email']
        mobile = recived_json_data['mobile']
        dept = recived_json_data['dept']
        
        employee = Employee()
        employee.name = name
        employee.mobile = mobile
        employee.dept = dept
        employee.email = email
        employee.created_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        employee.lastmodified_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        employee.save()
        
        return JsonResponse({"status":"success"})
        # messages.success(request, "The Employee "+ name +"Inserted Sucessfully")
        # return render(request,"create.html")
    else:
        return render(request,"create.html")