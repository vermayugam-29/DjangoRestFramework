from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('addStudent', post_student),
    path('updateStudent/<id>', update_student),
    path('deleteStudent/<id>', delete_student)
]
