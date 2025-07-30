from django import forms
from .models import Admission
from .models import AdminUser


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['name', 'phone', 'email', 'course', 'city', 'pincode']



class AdminLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


#add_course form

from django import forms
from .models import Course

# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['name', 'description']  # change as per your model
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'course_photo']


#add_staff form
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_name', 'staff_photo', 'course']
        widgets = {
            'staff_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter staff name'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
        }

#add_syllabus form
from django import forms
from .models import Syllabus

class SyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ['course', 'syllabus_pdf']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'syllabus_pdf': forms.FileInput(attrs={'class': 'form-control'}),
        }

#about us
# forms.py
from django import forms
from .models import AboutUs

class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter About Us content'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


#Salient feature form
#gallery form
from django import forms
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image title'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


#academy fetures form
# main/forms.py

# forms.py (if using ModelForm)
from django import forms
from .models import AcademyFeature

class AcademyFeatureForm(forms.ModelForm):
    class Meta:
        model = AcademyFeature
        fields = ['title', 'description', 'detailed_description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'detailed_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


# forms.py
#add student
# main/forms.py

from django import forms
from .models import Student

class StudentEntryForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['admission', 'phone', 'email', 'course', 'student_photo']
        widgets = {
            'admission': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'student_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# forms.py student
from django import forms

class StudentLoginForm(forms.Form):
    email = forms.EmailField(label="Enter Your Registered Email")




