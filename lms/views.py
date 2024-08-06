from django.shortcuts import render, redirect,HttpResponse
from myapp.EmailBackend import EmailBackEnd
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.models import CustomUser

def base(request):
    return render(request, "base.html")

def user_login(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == "POST":
       user = EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
       if user!=None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect('hod/home')
           elif user_type == '2':
               return HttpResponse('This is Staff Panel')
           elif user_type == '3':
               return HttpResponse('This is Student Panel')
           else:
               messages.error(request,'Email and Password Are Invalid !')
               return redirect('user_login')
       else:
           messages.error(request,'Email and Password Are Invalid !')
           return redirect('user_login')
		   


def doLogout(request):
    logout(request)
    return redirect('user_login')

def profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    
    context={
        'user':user
    }
    return render(request,'profile.html',context)


# def profile_update(request):
#     if request.method == "POST":
#         profile_pic = request.FILES.get('profile_pic')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         #email = request.POST.get('email')
#         #username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         try:
#             customuser = CustomUser.objects.get(id = request.user.id)

#             customuser.first_name = first_name
#             customuser.last_name = last_name

#             if password !=None and password != "":
#                 customuser.set_password(password)
#             if profile_pic !=None and profile_pic != "":
#                 customuser.profile_pic = profile_pic
#             customuser.save()
#             messages.success(request,'Your Profile Updated Successfully !')
#             return redirect('profile')
#         except:
#             messages.error(request,'Failed To Update Your Profile')

#     return render(request,'profile.html')
	

def add_student(request):
    return render(request,'hod/add_student.html')




@login_required(login_url='/')
def profile(request):
    user = CustomUser.objects.get(id = request.user.id)


    context = {
        "user":user,
    }
    return render(request,'profile.html',context)

@login_required(login_url='/')
def profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #email = request.POST.get('email')
        #username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic)
        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name

            if password !=None and password != "":
                customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request,'Failed To Update Your Profile')

    return render(request,'profile.html')
	
	


