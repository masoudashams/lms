
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Course, CustomUser, Student,Staff
from django.contrib import messages
from pyttsx3 import Engine

engine = Engine()
@login_required(login_url='/')
def home(request):
    student_count=Student.objects.all().count()
    staff_count=Staff.objects.all().count()
    course_count=Course.objects.all().count()
    context={

        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,

    }



    return render(request,'hod/home.html',context)



@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
   

    if request.method == "POST":
        # profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')

      

        if CustomUser.objects.filter(email=email).exists():
           messages.warning(request,'Email Is Already Taken')
           return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
           messages.warning(request,'Username Is Already Taken')
           return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                # profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
          

            student = Student(
                admin = user,
                address = address,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_student')

    context = {
        'course':course,
        
    }
    return render(request,'hod/add_student.html', context)
	




@login_required(login_url='/')
def view_student(request):
    student = Student.objects.all()
    context={
    'student':student
    }

    return render(request,'hod/view_student.html',context)



@login_required(login_url='/')
def edit_student(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()


    context = {
        'student':student,
        'course':course,
       
    }
    return render(request,'hod/edit_student.html',context)
      



@login_required(login_url='/')
def update_student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        # profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        # session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

    

        student.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_student')

    return render(request,'hod/edit_student.html')

	




@login_required(login_url='/')
def delete_student(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('view_student')
	


# course section


@login_required(login_url='/')
def add_course(request):

    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Course Are Successfully Created ')

        # engine.say("course are successfully added")

        # engine.runAndWait()
        # engine.endLoop()
        return redirect('view_course')

    return render(request,'hod/add_course.html')



@login_required(login_url='/')
def view_course(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,'hod/view_course.html',context)



@login_required(login_url='/')
def edit_course(request, id):
    try:
        course = Course.objects.get(id=id)
    except Course.DoesNotExist:
        messages.error(request, "Course not found.")
        return redirect('view_course')

    context = {
        'course': course,
    }
    return render(request, 'hod/edit_course.html', context)



@login_required(login_url='/')
def update_course(request):
    if request.method == "POST":
       name=request.POST.get('name')
       course_id=request.POST.get('course_id')


       course=Course.objects.get(id=course_id)
       course.name=name
       course.save()
       messages.success(request,'Course is Successfully Updated')
       return redirect('view_course')

    return render(request,'hod/edit_course.html')



@login_required(login_url='/')
def delete_course(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Course are Successfully Deleted')

    return redirect('view_course')





def add_staff(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"Email is already taken")
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"username is already taken")
            return redirect('add_staff')
        else:
            user=CustomUser(first_name=first_name,last_name=last_name,email=email, username =username , user_type=2)
            user.set_password(password)
            user.save()


            staff=Staff(
                admin=user,
                address=address,
                gender=gender
            )
            staff.save()
            messages.success(request,"Instructor is Sucessfully added")
            return redirect('add_staff')
    return render(request,'hod/add_staff.html')



def view_staff(request):
    staff=Staff.objects.all()

    context={
        'staff':staff
    }
    return render(request,'hod/view_staff.html',context)


def edit_staff(request,id):
    staff=Staff.objects.get(id=id)

    context={
        'staff':staff
    }

    return render(request,'hod/edit_staff.html',context)





def update_staff(request):
    if request.method=="POST":
        staff_id=request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user=CustomUser.objects.get(id=staff_id)
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.email=email

        if password != None and password != "":
            user.set_password(password)
        user.save()

        staff=Staff.objects.get(admin=staff_id)
        staff.gender=gender
        staff.address=address

        staff.save()
        messages.success(request,"Staff Data successfully Updated")
        return redirect ('view_staff')

    return render(request,'hod/edit_staff.html')
