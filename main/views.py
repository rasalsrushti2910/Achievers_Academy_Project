from django.shortcuts import render, redirect
from .models import Admission
from django.contrib import messages
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



@login_required
def receptionist_dashboard(request):
    # Fetch all admissions sorted by course, then name
    admissions = Admission.objects.all().order_by('name', 'submitted_at' )

    # Group data by submission date
    grouped_data = defaultdict(list)
    for admission in admissions:
        date_key = admission.submitted_at.date()  # Grouping key: date only
        grouped_data[date_key].append(admission)

    # Convert defaultdict to regular dict
    context = {
        'grouped_admissions': dict(grouped_data)
    }
    return render(request, 'main/receptionist_dashboard.html', context)


def receptionist_logout(request):
    logout(request)
    return redirect("receptionist_login")