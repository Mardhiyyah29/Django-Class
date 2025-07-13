from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name="home"),
    path('dashboard', views.task_list,name="task-list"),
    path('about/', views.About,name="about"),
    path('service/', views.Service,name="service"),
    path('contact/', views.Contact,name="contact"),
    path('signup/', views.signup,name="signup"),
    path('task/new/', views.task_create, name='task-create'),
    path('task/delete/<int:task_id>', views.task_delete, name='task-delete'),



  #  path('contact/', views.Contact,name="contact"),
    #  path('contact/', views.Contact,name="contact"),




]
