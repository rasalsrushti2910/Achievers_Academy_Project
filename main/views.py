from django.shortcuts import render, redirect
from .models import Admission
from django.contrib import messages

#   AdmissionForm  view

from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdmissionForm  # You'll need to create this form

def home(request):
    return render(request, 'main/home.html')

def admission_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        course = request.POST.get("course")
        state = request.POST.get("state")
        district = request.POST.get("district")
        subdistrict = request.POST.get("subdistrict")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        message = request.POST.get("message")

        Admission.objects.create(
            name=name, phone=phone, email=email, course=course,
            state=state, district=district, subdistrict=subdistrict,
            city=city, pincode=pincode, message=message
        )
        
        messages.success(request, 'Your admission form has been submitted successfully!')
        return redirect('admission_form')  # Use your URL name

    return render(request, "main/admission_form.html")


# Explore courses
def english_course(request):
    return render(request, 'main/english_course.html')



def japanese_course(request):
    return render(request, 'main/japanese_course.html')

def german_course(request):
    return render(request, 'main/german_course.html')



# receptionist_login & logout Dashboard,edit and delete View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from collections import defaultdict
def receptionist_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("receptionist_dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "main/receptionist_login.html")

from collections import defaultdict, OrderedDict
from django.shortcuts import render
from .models import Admission
from collections import defaultdict
from django.utils import timezone
from datetime import timedelta
from .models import Admission  # Make sure you're using the correct model

def receptionist_dashboard(request):
    grouped_admissions = defaultdict(list)
    all_admissions = Admission.objects.all().order_by('-submitted_at')  # Use correct date field

    for admission in all_admissions:
        # Group by week starting Monday
        week_start = admission.submitted_at - timedelta(days=admission.submitted_at.weekday())
        week_label = week_start.strftime('%B %d, %Y')  # e.g., "July 22, 2025"
        grouped_admissions[week_label].append(admission)

    return render(request, 'main/receptionist_dashboard.html', {
        'grouped_admissions': dict(grouped_admissions)
    })


def receptionist_logout(request):
    logout(request)
    return redirect("receptionist_login")

def edit_admission(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id)
    if request.method == 'POST':
        form = AdmissionForm(request.POST, instance=admission)
        if form.is_valid():
            form.save()
            return redirect('receptionist_dashboard')  # Update this to your dashboard view name
    else:
        form = AdmissionForm(instance=admission)
    # return render(request, 'edit_admission.html', {'form': form})
    return render(request, 'main/edit_admission.html', {'form': form})


def delete_admission(request, admission_id):
    admission = get_object_or_404(Admission, id=admission_id)
    admission.delete()
    return redirect('receptionist_dashboard')  # Update this to your dashboard view name


#Admin_login & logout Dashboard,edit and delete View

from .forms import AdminLoginForm
from .models import AdminUser

def admin_login(request):
    error = ''
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                admin = AdminUser.objects.get(username=username, password=password)
                request.session['admin_id'] = admin.id
                return redirect('admin_dashboard')
            except AdminUser.DoesNotExist:
                error = 'Invalid credentials'
    else:
        form = AdminLoginForm()

    return render(request, 'main/admin_login.html', {'form': form, 'error': error})

def admin_dashboard(request):
    if not request.session.get('admin_id'):
        return redirect('admin_login')
    return render(request, 'main/admin_dashboard.html')


from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm

# def add_course(request):
#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('view_course')
#     else:
#         form = CourseForm()
#     return render(request, 'main/admin/add_course.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CourseForm
from .models import Course

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('add_course')
    else:
        form = CourseForm()
    
    return render(request, 'main/admin/add_course.html', {'form': form})



# def view_course(request):
#     courses = Course.objects.all()
#     return render(request, 'main/admin/view_course.html', {'courses': courses})

# def edit_course(request, course_id):
#     course = get_object_or_404(Course, id=course_id)

#     if request.method == 'POST':
#         course.name = request.POST.get('name')
#         course.description = request.POST.get('description')
#         course.save()
#         messages.success(request, 'Course updated successfully!')
#         return redirect('view_course')  # Adjust to your actual URL name

#     return render(request, 'main/admin/edit_course.html', {'course': course})

# def delete_course(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     course.delete()
#     messages.success(request, "Course deleted successfully.")
#     return redirect('view_course')  # Update with your actual URL name

from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm
from django.contrib import messages

def view_course(request):
    courses = Course.objects.all()
    return render(request, 'main/admin/view_course.html', {'courses': courses})

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('view_course')
    else:
        form = CourseForm(instance=course)
    return render(request, 'main/admin/edit_course.html', {'form': form})


def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    messages.success(request, 'Course deleted successfully!')
    return redirect('view_course')




#for add_staff view
from .forms import StaffForm
from django.contrib import messages

def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff added successfully!')
            return redirect('add_staff')  # or redirect to view_staff
    else:
        form = StaffForm()
    return render(request, 'main/admin/add_staff.html', {'form': form})

from .models import Staff

def view_staff(request):
    staff_list = Staff.objects.all()
    return render(request, 'main/admin/view_staff.html', {'staff_list': staff_list})

def edit_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff updated successfully!')
            return redirect('view_staff')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'main/admin/edit_staff.html', {'form': form})

def delete_staff(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    staff.delete()
    messages.success(request, 'Staff deleted successfully!')
    return redirect('view_staff')


#for syllabus 

from .forms import SyllabusForm
from django.contrib import messages

def add_syllabus(request):
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Syllabus added successfully!')
            return redirect('add_syllabus')
    else:
        form = SyllabusForm()
    return render(request, 'main/admin/add_syllabus.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Syllabus
from .forms import SyllabusForm

# View All Syllabus
def view_syllabus(request):
    syllabus_list = Syllabus.objects.select_related('course')
    return render(request, 'main/admin/view_syllabus.html', {'syllabus_list': syllabus_list})

# Edit Syllabus
def edit_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, pk=syllabus_id)
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES, instance=syllabus)
        if form.is_valid():
            form.save()
            messages.success(request, 'Syllabus updated successfully!')
            return redirect('view_syllabus')
    else:
        form = SyllabusForm(instance=syllabus)
    return render(request, 'main/admin/edit_syllabus.html', {'form': form})

# Delete Syllabus
def delete_syllabus(request, syllabus_id):
    syllabus = get_object_or_404(Syllabus, pk=syllabus_id)
    syllabus.delete()
    messages.success(request, 'Syllabus deleted successfully!')
    return redirect('view_syllabus')




#about us 
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import AboutUs
from .forms import AboutUsForm

def add_or_edit_about_us(request, pk=None):
    if pk:
        about_us = get_object_or_404(AboutUs, pk=pk)
    else:
        about_us = None

    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance=about_us)
        if form.is_valid():
            form.save()
            return redirect('add_about_us')  # Redirect to same page
    else:
        form = AboutUsForm(instance=about_us)

    all_about = AboutUs.objects.all()

    return render(request, 'main/admin/add_about_us.html', {
        'form': form,
        'about_us_entries': all_about,
    })

    return render(request, 'main/admin/add_about_us.html', context)

#Salient fetures view

#gallery view
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import GalleryForm
from .models import Gallery

from django.shortcuts import render, redirect, get_object_or_404

# Add Gallery Image
def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded successfully!")
            return redirect('view_gallery')
    else:
        form = GalleryForm()
    return render(request, 'main/admin/add_gallery.html', {'form': form})




def view_gallery(request):
    images = Gallery.objects.all()
    return render(request, 'main/admin/view_gallery.html', {'images': images})

def edit_gallery(request, pk):
    image = get_object_or_404(Gallery, pk=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "Gallery image updated successfully.")
            return redirect('view_gallery')
    else:
        form = GalleryForm(instance=image)
    return render(request, 'main/admin/edit_gallery.html', {'form': form})

def delete_gallery(request, pk):
    image = get_object_or_404(Gallery, pk=pk)
    image.delete()
    messages.success(request, "Gallery image deleted.")
    return redirect('view_gallery')

#acdemy features view


from django.shortcuts import render, redirect, get_object_or_404
from .models import AcademyFeature
from django.contrib import messages

def add_academy_feature(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        detailed_description = request.POST['detailed_description']

        AcademyFeature.objects.create(
            title=title,
            description=description,
            detailed_description=detailed_description
        )
        messages.success(request, "Academy Feature added successfully!")
        return redirect('add_academy_feature')

    return render(request, 'main/admin/add_academy_feature.html')


def view_academy_features(request):
    features = AcademyFeature.objects.all()
    return render(request, 'main/admin/view_academy_features.html', {'features': features})


def edit_academy_feature(request, pk):
    feature = get_object_or_404(AcademyFeature, pk=pk)
    if request.method == 'POST':
        feature.title = request.POST['title']
        feature.description = request.POST['description']
        feature.detailed_description = request.POST['detailed_description']
        feature.save()
        messages.success(request, "Academy Feature updated successfully!")
        return redirect('view_academy_features')

    return render(request, 'main/admin/edit_academy_feature.html', {'feature': feature})


def delete_academy_feature(request, pk):
    feature = get_object_or_404(AcademyFeature, pk=pk)
    feature.delete()
    messages.success(request, "Academy Feature deleted successfully!")
    return redirect('view_academy_features')


# views.py
#add student
from django.shortcuts import render, redirect
from .forms import StudentEntryForm
from .models import Admission

def add_student(request):
    admissions = Admission.objects.all()
    if request.method == 'POST':
        form = StudentEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('add_student')
    else:
        form = StudentEntryForm()
    return render(request, 'main/admin/add_student.html', {
        'form': form,
        'admissions': admissions
    })


from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentEntryForm
from django.contrib import messages

def view_student(request):
    students = Student.objects.all()
    return render(request, 'main/admin/view_student.html', {'students': students})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    admissions = Admission.objects.all()

    if request.method == 'POST':
        form = StudentEntryForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('view_student')
    else:
        form = StudentEntryForm(instance=student)

    return render(request, 'main/admin/edit_student.html', {
        'form': form,
        'student': student,
        'admissions': admissions
    })

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('view_student')


#student login view

# views.py
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentLoginForm
from django.contrib import messages

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                student = Student.objects.get(email=email)
                request.session['student_id'] = student.id
                return redirect('student_dashboard')
            except Student.DoesNotExist:
                messages.error(request, "Email not found. Please contact admin.")
    else:
        form = StudentLoginForm()
    return render(request, 'main/student_login.html', {'form': form})



def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    return render(request, 'main/student_dashboard.html', {'student': student})



from django.shortcuts import render
from main.models import Course  # Assuming model name is Course

def student_view_courses(request):
    courses = Course.objects.all()
    return render(request, 'main/student/view_courses.html', {'courses': courses})


# views.py
from django.shortcuts import render
from .models import Staff  # Assuming your model name is Staff

def view_staff1(request):
    staff_members = Staff.objects.all()
    return render(request, 'main/student/view_staff1.html', {'staff_members': staff_members})

# views.py
from django.shortcuts import render
from .models import Syllabus

def view_syllabus1(request):
    syllabus_entries = Syllabus.objects.select_related('course').all()
    return render(request, 'main/student/view_syllabus1.html', {'syllabus_entries': syllabus_entries})

# views.py
from django.shortcuts import render
from .models import AcademyFeature

def view_academy_features1(request):
    features = AcademyFeature.objects.all()
    return render(request, 'main/student/view_academy_features1.html', {'features': features})



from django.shortcuts import render
from .models import Course

def home(request):
    courses = Course.objects.all()
    return render(request, 'main/home.html', {'courses': courses})


from main.models import AboutUs

def home(request):
    courses = Course.objects.all()  # If used
    all_about= AboutUs.objects.all()
    return render(request, 'main/home.html', {
        'courses': courses,
        'all_about': all_about,
    })

from django.shortcuts import render
from .models import AcademyFeature

def home(request):
    courses = Course.objects.all()  # If used
    all_about= AboutUs.objects.all()
    features = AcademyFeature.objects.all()
    return render(request, 'main/home.html', {
        'courses': courses,
        'all_about': all_about,
        'academy_features': features
    })

from .models import Gallery

from django.shortcuts import render
from .models import Gallery, Course, AboutUs, AcademyFeature  # adjust as per your app

def home(request):
    gallery_images = Gallery.objects.all()
    courses = Course.objects.all()  # If used
    all_about= AboutUs.objects.all()
    features = AcademyFeature.objects.all()
    return render(request, 'main/home.html', {
        'gallery_images': gallery_images,
        'courses': courses,
        'all_about': all_about,
        'academy_features': features
    })

def created_by(request):
    return render(request, 'main/created_by.html')




















