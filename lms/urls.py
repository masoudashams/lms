"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,staff_views,student_views,hod_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name="base"),
    path('',views.user_login, name="user_login"),
    path('doLogin',views.doLogin, name="doLogin"),
    path('doLogout',views.doLogout,name='logout'),
    path('hod/home',hod_views.home, name='home'),
    path('profile',views.profile, name="profile"),
    path('profile/update',views.profile_update, name="profile_update"),
    path('hod/Student/Add',hod_views.add_student,name='add_student'),
    path('hod/Student/View',hod_views.view_student,name='view_student'),
    path('hod/Student/Edit/<str:id>',hod_views.edit_student,name='edit_student'),
    path('hod/Student/Update',hod_views.update_student,name='update_student'),
    path('hod/Student/Delete/<str:admin>',hod_views.delete_student,name='delete_student'),
    path('hod/Course/Add',hod_views.add_course,name='add_course'),
    path('hod/Course/View',hod_views.view_course,name='view_course'),
    path('hod/Course/Edit/<str:id>',hod_views.edit_course,name='edit_course'),
    path('hod/Course/Update',hod_views.update_course,name='update_course'),
    path('hod/Course/Delete/<str:id>',hod_views.delete_course,name='delete_course'),
    path('hod/Staff/Add',hod_views.add_staff,name='add_staff'),
    path('hod/Staff/View',hod_views.view_staff, name='view_staff'),
    path('hod/Staff/Edit/<str:id>',hod_views.edit_staff,name='edit_staff'),
    path('hod/Staff/Update',hod_views.update_staff,name='update_staff'),
    # path('hod/Staff/Delete/<str:id>',hod_views.delete_staff,name='delete_staff'),
    
 



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
