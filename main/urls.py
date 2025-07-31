from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('admission/', views.admission_form, name='admission_form'),


     path('english_course', views.english_course, name='english_course'),
    path('japanese_course', views.japanese_course, name='japanese_course'),
    path('german_course', views.german_course, name='german_course'),

    path('receptionist/login/', views.receptionist_login, name='receptionist_login'),
    path('receptionist_dashboard/', views.receptionist_dashboard, name='receptionist_dashboard'),
    path('receptionist/logout/', views.receptionist_logout, name='receptionist_logout'),

   
    path('receptionist/dashboard/<int:admission_id>/', views.edit_admission, name='edit_admission'),
    path('receptionist/delete/<int:admission_id>/', views.delete_admission, name='delete_admission'),

    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),



    path('add_course/', views.add_course, name='add_course'),
    path('view_course/', views.view_course, name='view_course'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),


    path('add_staff/', views.add_staff, name='add_staff'),
    path('view_staff/', views.view_staff, name='view_staff'),
    path('edit_staff/<int:staff_id>/', views.edit_staff, name='edit_staff'),
    path('delete_staff/<int:staff_id>/', views.delete_staff, name='delete_staff'),

     path('add_syllabus/', views.add_syllabus, name='add_syllabus'),
    
    path('view_syllabus/', views.view_syllabus, name='view_syllabus'),
    path('edit_syllabus/<int:syllabus_id>/', views.edit_syllabus, name='edit_syllabus'),
    path('delete_syllabus/<int:syllabus_id>/', views.delete_syllabus, name='delete_syllabus'),
  
   
    path('add_about_us/', views.add_or_edit_about_us, name='add_about_us'),
    path('add_about_us/<int:pk>/', views.add_or_edit_about_us, name='add_about_us_with_pk'),

    path('add_gallery/', views.add_gallery, name='add_gallery'),
    path('view_gallery/', views.view_gallery, name='view_gallery'),

    path('edit_gallery/<int:pk>/', views.edit_gallery, name='edit_gallery'),
    path('delete_gallery/<int:pk>/', views.delete_gallery, name='delete_gallery'),
 
    path('add_academy_feature/', views.add_academy_feature, name='add_academy_feature'),
    path('view_academy_features/', views.view_academy_features, name='view_academy_features'),
    path('edit_academy_feature/<int:pk>/', views.edit_academy_feature, name='edit_academy_feature'),
    path('delete_academy_feature/<int:pk>/', views.delete_academy_feature, name='delete_academy_feature'),

    path('add_student/', views.add_student, name='add_student'),
    path('view_student/', views.view_student, name='view_student'),
    path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),

    path('student_login/', views.student_login, name='student_login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),

    path('view_courses/', views.student_view_courses, name='student_view_courses'),  
    path('view_staff1/', views.view_staff1, name='view_staff1'), 
    path('view_syllabus1/', views.view_syllabus1, name='view_syllabus1'),
    path('view_academy_features1/', views.view_academy_features1, name='view_academy_features1'),
    
    path('created_by/', views.created_by, name='created_by'),   
   
]









    




   

   