from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import StudentForm
from django.contrib import messages
from .models import Student,Trainer,Task
import datetime
def home(request):
    return render(request,"index.html")
def signup(request):
    if request.method=='POST':
        form=StudentForm(data=request.POST,files=request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            messages.info(request,"registration failed")
            form=StudentForm()
            return render(request,"signup.html",{'form':form})
    else:
        form=StudentForm()
        return render(request,"signup.html",{'form':form})
        
def slogin(request):
    username=request.POST['username']
    password=request.POST['password']
    user=Student.objects.filter(username=username,password=password).get()
    if user is not None:
        auth.login(request,user)
        return render(request,'shome.html')
    else:
        messages.info(request,'Invalid username and password')
        return redirect("/")

def tsignup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        mobile=request.POST['mobile']
        t=Trainer.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        t.mobile=mobile
        t.save()
        messages.info(request,'signed up sucessfully')
        return redirect("/trainer")
    else:
        return render(request,'tsignup.html')

def tlogin(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        st=Student.objects.all()
        return render(request,'thome.html',{'st':st})
    else:
        messages.info(request,'Invalid username and password')
        return redirect("/trainer")

def submittask(request):
    t=Task()
    uname=request.POST['username']
    student=Student.objects.filter(username=uname).get()
    t.student_id=student
    t.topics=request.POST['topics']
    t.timings_for_day=request.POST['timing']
    t.date=datetime.datetime.now()
    t.remarks="no comments"
    t.save()
    auth.logout(request)
    messages.info(request,"sucessfully submitted")
    return redirect("/")

def viewremarks(request):
    uname=request.GET['uname']
    student=Student.objects.filter(username=uname).get()
    data=Task.objects.filter(student_id=student).all()
    return render(request,'showtask.html',{'data':data})

def trainer(request):
    return render(request,'trainer.html')

# def shome(request):
#     return render(request, 'shome.html')
    
