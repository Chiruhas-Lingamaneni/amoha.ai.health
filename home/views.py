
from django.shortcuts import render
from home.forms import UserForm,UserProfileInfoForm,UserImageForm,UserQueryForm
from home.models import UserSignupDb,UserQuery
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

def register(request):
    registered=True
    if request.method=="POST":

        userform=UserForm(data=request.POST)
        userInfo=UserProfileInfoForm(data=request.POST)
        if userform.is_valid() and userInfo.is_valid():
            
            user_data=userform.save(commit=False)
            user_data.set_password(user_data.password)

            userprofile=userInfo.save(commit=False)
            user_data.save()
            userprofile.user=user_data
            userprofile.save()
            registered=False
        else:
            return render(request,'signin.html',{'registered':registered,
                                                'userform':userform,
                                                'userinfoform':userInfo}
                                                )            
    
    userform=UserForm
    userinfoform=UserProfileInfoForm
    return render(request,'signin.html',{'registered':registered,
                                            'userform':userform,
                                            'userinfoform':userinfoform})
@login_required
def uploadimg(request):
    uploaded=True
    if request.method=="POST":
        userpic=UserImageForm(data=request.POST)
        if userpic.is_valid():

            saveto=User.objects.get(username=request.user)
            
            usersave=userpic.save(commit=False)
            usersave.name=saveto
            usersave.dateOfUpload=datetime.date.today()
            usersave.timeOfUpload=datetime.datetime.now().time()
            usersave.patienteye=request.FILES['patienteye']
            usersave.save()
            uploaded=False

    return render(request,'upload.html',{'form':UserImageForm,'uploaded':uploaded})

def index(request):
    return render(request,'index.html')


def userlogin(request):

    invalid=False
    if request.method=="POST":

        global uname
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_log=authenticate(username=username,password=password)
        if user_log:
            if user_log.is_active:
                login(request,user_log)
                uname=username
                return HttpResponseRedirect(reverse(index))
            else:
                print("User not active")
        else:
            print("Wrong cradentials")
            invalid=True

    return render(request,'login.html',{"invalid":invalid})

@login_required
def logedin(request):

    global uname
    #shodata=UserSignupDb.objects.get(user = uname)

    shodata = UserSignupDb.objects.get(user=User.objects.get (username=request.user))
    uname=User.objects.get (username=request.user)
    #print(dir(shodata))
    finaldata={'name':uname.username,'age':shodata.age,'mobileNumber':shodata.mobileNumber,'gender':shodata.gender}
    print(finaldata)
    return render(request,'userdetail.html',finaldata)

@login_required
def logedout(request):
    global uname
    logout(request)
    return HttpResponseRedirect(reverse(index))

def getintouch(request):

    #form=UserQueryForm()
    saved=False
    if request.method == 'POST':
        name =request.POST.get('qname')
        email=request.POST.get("qemail")
        mobileNumber=int(request.POST.get("qphone"))
        organisation=request.POST.get("qorga")
        message=request.POST.get("qmessage")
        query=UserQuery.objects.get_or_create(name=name,email=email,mobileNumber=mobileNumber,organisation=organisation,message=message)[0]
        query.save()
        #if form.is_valid():
        #form.save()
        saved=True
        #else:
        print("form not valid")
        #print(form.is_valid())
    return render(request,'query.html',{'saved':saved})