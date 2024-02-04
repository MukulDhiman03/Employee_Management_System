from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp  # Import the Emp model


# Create your views here.
def emp_home(request):
    
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{
        'emps':emps,
    })

def add_emp(request):
    if request.method=="POST":
        # data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_address=request.POST.get("emp_address")
        emp_phone=request.POST.get("emp_phone")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")
        
        
        
        
        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.working=emp_working
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        
        #save the object
        e.save()
        
        
        
        
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})


def delete_emp(request,emp_id):
    # print(emp_id)
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")
    