from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('admission/', views.admission_form, name='admission_form'),


     path('english_course', views.english_course, name='english_course'),
    path('japanese_course', views.japanese_course, name='japanese_course'),
    path('german_course', views.german_course, name='german_course'),

    path('receptionist/login/', views.receptionist_login, name='receptionist_login'),
    path('receptionist/dashboard/', views.receptionist_dashboard, name='receptionist_dashboard'),
    path('receptionist/logout/', views.receptionist_logout, name='receptionist_logout'),

   
    path('receptionist/dashboard/<int:admission_id>/', views.edit_admission, name='edit_admission'),
    path('receptionist/delete/<int:admission_id>/', views.delete_admission, name='delete_admission'),

    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]



    




   

   