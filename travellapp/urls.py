
from django.urls import path

from travellapp import views

urlpatterns = [

    path('',views.demo,name='index')
]