from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth



def login(request):
    if request.method=="POST":
        username = request.POST['username'] 
        password = request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("====================a============================")
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            print("====================b===========================")
            return redirect('login')
    else:
        print("====================c===========================")
        return render(request,'login.html')




def register(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                print("created user")
                return redirect('/')
        else:
            print("password not matched")
            return redirect('register')

    else:
        return render(request,"registration.html")







def logout(request):
    auth.logout(request)
    return redirect('/')                