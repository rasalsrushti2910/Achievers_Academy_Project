from django.db import models
class Admission(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    course = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    state = models.CharField(max_length=100, default='Maharashtra')
    district = models.CharField(max_length=100, default='Kolhapur')
    subdistrict = models.CharField(max_length=100, default='Hatkanangale')
    city = models.CharField(max_length=100, default='Kolhapur')
    pincode = models.CharField(max_length=6, default='416003')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AdminUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
#Add_course model 
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    course_photo = models.ImageField(upload_to='course_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

#staff model
class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    staff_photo = models.ImageField(upload_to='staff_photos/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name
    
#syllabus model

from django.db import models
from .models import Course  # Ensure Course model is already defined

class Syllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    syllabus_pdf = models.FileField(upload_to='syllabus_pdfs/')

    def __str__(self):
        return f"Syllabus for {self.course.name}"
    
#about us

from django.db import models

class AboutUs(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='about_us_images/', blank=True, null=True)

    def __str__(self):
        return "About Us Section"

#Gallery model
from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return self.title
    
 #academy fetures
from django.db import models
from django.db import models

class AcademyFeature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    detailed_description = models.TextField()

    def __str__(self):
        return self.title
    

from django.db import models
class Student(models.Model):
    admission = models.ForeignKey('Admission', on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(unique=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    student_photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)

    def __str__(self):
        return self.admission.name  # Adjust based on your Admission model






