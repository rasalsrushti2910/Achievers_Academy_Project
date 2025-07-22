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



# receptionist_login & Dashboard View

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

def receptionist_dashboard(request):
    # Fetch all admissions ordered by name and submitted date
    admissions = Admission.objects.all().order_by('name', 'submitted_at')

    # Group admissions by date
    grouped_data = defaultdict(list)
    for admission in admissions:
        date_key = admission.submitted_at.date()
        grouped_data[date_key].append(admission)

    # Sort the grouped data by date (descending)
    sorted_grouped_admissions = OrderedDict(sorted(grouped_data.items(), reverse=True))

    # Pass the sorted data to the template
    context = {
        'grouped_admissions': sorted_grouped_admissions
    }
    return render(request, 'main/receptionist_dashboard.html', context)

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


#Admin_login & Dashboard View

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

#For Course







