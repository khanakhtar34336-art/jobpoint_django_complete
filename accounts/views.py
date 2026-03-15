from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Profile 
from django.contrib.auth import authenticate, login
from jobs.models import Application
from jobs.models import Job
from .forms import ProfileForm
from django.contrib.auth import logout
from .models import Connection
from django.contrib.auth.models import User



User = get_user_model()
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Username and Password required!")
            return redirect('accounts:login')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('accounts:register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name
        )

        login(request, user)
        messages.success(request, "Account Created Successfully!")
    return redirect("accounts:profile")


@login_required
def dashboard(request):
    jobs = Job.objects.all()
    profile = request.user.profile
    applied_jobs = Application.objects.filter(user=request.user)
    connections = Connection.objects.filter(receiver=request.user, status="pending")


    total_jobs = Job.objects.count()
    total_users = User.objects.count()
    total_applications = Application.objects.count()
    return render(request, 'dashboard.html', {
        'jobs': jobs,
        'profile' : profile,
        "applied_jobs": applied_jobs,
        'connections': connections,
        
        'total_jobs': total_jobs,
        'total_users': total_users,
        'total_applications': total_applications,

        })

@login_required
def profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        request.user.first_name = request.POST.get('first_name') 
        request.user.email = request.POST.get('email') 
        request.user.save()

        profile.contact = request.POST.get('contact') 
        profile.about = request.POST.get('about') 
        profile.degree = request.POST.get('degree') 
        profile.institute = request.POST.get('institute') 
        profile.graduation_year = request.POST.get('graduation_year') 

        profile.full_name = request.POST.get("full_name")
        profile.bio = request.POST.get("bio")
        profile.location = request.POST.get("location")

        if request.FILES.get('profile_photo'):
            profile.profile_photo = request.FILES.get('profile_photo')

        if request.FILES.get('resume'):
            profile.resume = request.FILES.get('resume')

        profile.save()
        

        messages.success(request, "Profile Updated Successfully!")
        return redirect('accounts:dashboard')

    return render(request, 'profile.html', {'profile': profile})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('accounts:login')
    return render(request, 'login.html')

def login_redirect(request):
    return redirect('profile')

def create_profile(request):
    if request.method == "POST":
        contact = request.POST.get('contact')
        about = request.POST.get('about')
        degree = request.POST.get('degree')
        institute = request.POST.get('institute')
        graduation_year = request.POST.get('graduation_year')

        profile = Profile.objects.get(user=request.user)

        profile.contact = contact
        profile.about = about
        profile.degree = degree
        profile.institute = institute
        profile.graduation_year = graduation_year
        profile.save()

        messages.success(request, "Profile created successfully")

        return redirect('/jobs/')   # ✅ direct redirect

    return render(request, "create_profile.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def send_connection(request, user_id):

    receiver = User.objects.get(id=user_id)

    Connection.objects.get_or_create(
        sender=request.user,
        receiver=receiver
    )

    return redirect("dashboard")

@login_required
def accept_connection(request, conn_id):

    connection = Connection.objects.get(id=conn_id)

    connection.status = "accepted"
    connection.save()

    return redirect("dashboard")