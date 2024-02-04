from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        print(name)
    
    date=datetime.datetime.now()
    print("Test function called from view")
    # return HttpResponse("<h1>Hello this is index page</h1>"+str(date))
    
    student_data={
        'student_name':'Mukul Dhiman',
        'student_college':'GEU',
        'student_city':'Roorkee'
    }
    list_of_programs=[
        'DSA',
        'CP',
        'WEB DEV',
    ]
    
    isActive=True
    
    data={
        'date':date,
        'student_data':student_data,
        'list_of_programs':list_of_programs,
        'isActive':isActive
    }
    
    return render(request,"home.html",data)

def about(request):
    return render(request,"about.html",{})

def service(request):
    return render(request,"service.html",{})

    