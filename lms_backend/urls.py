"""
URL configuration for lms_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from accounts.views import TrainerSignUpView,TrainerRetreiveUpdateView

from course_management.views import CourseCreateListView,CourseRetreiveUpdateDeleteView

from module_management.views import ModuleCreateView,ModuleRetreiveUpdateDeleteView

from lesson_management.views import LessonCreateView,LessonRetreiveUpdateDeleteView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),

    #accounts
    path('trainer/signup/',TrainerSignUpView.as_view()),
    path('trainer/profile/',TrainerRetreiveUpdateView.as_view()),

    # token
    path('token/',ObtainAuthToken.as_view()),

    #course
    path('trainer/courses/',CourseCreateListView.as_view()),
    path('trainer/courses/<int:pk>/',CourseRetreiveUpdateDeleteView.as_view()),

    #modules
    path('courses/<int:pk>/modules/',ModuleCreateView.as_view()),
    path('modules/<int:pk>/',ModuleRetreiveUpdateDeleteView.as_view()),

    #lessons

    path('modules/<int:pk>/lessons/',LessonCreateView.as_view()),
    path('lessons/<int:pk>/',LessonRetreiveUpdateDeleteView.as_view()),




]
