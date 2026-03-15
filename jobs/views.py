
from django.shortcuts import  get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Job, Application, Message
from django.core.paginator import Paginator
from django.contrib.auth.models import User



def home(request):
    return render(request, 'index.html')


@login_required
def add_job(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        Job.objects.create(
            title=title,
            description=description,
            created_by=request.user
        )

        messages.success(request, "New job uploaded successfully!")

        return redirect("job_list")

    return render(request, "add_job.html")

def job_list(request):
    jobs = Job.objects.all()
   

    search = request.GET.get('search')
    location = request.GET.get('location')


    if search:
        jobs = jobs.filter(title__icontains=search)

    if location:
        jobs = jobs.filter(location__icontains=location)

    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    applied_jobs = []

    if request.user.is_authenticated:
        applied_jobs = Application.objects.filter(user=request.user).values_list('job_id', flat=True)

    return render(request, "jobs/job_list.html", {
        "jobs": jobs,
        "page_obj": page_obj,
        "applied_jobs": applied_jobs
    })

def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        resume = request.FILES.get("resume")
        if Application.objects.filter(job=job, user=request.user).exists():
          messages.error(request, "You already applied for this job")
          return redirect("job_list")


        Application.objects.get_or_create(
            job=job,
            user=request.user,
            resume=resume
        )
        messages.success(request, "Application submitted successfully!")
        return redirect("dashboard")

    return render(request, "apply_job.html", {"job": job})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def dashboard(request):

    applications = Application.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'applications': applications
    })

def feed(request):
    return render(request, 'feed.html')

@login_required
def profile(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')

        request.user.first_name = first_name
        request.user.email = email
        request.user.save()

        messages.success(request, "Profile Updated Successfully!")
    if not hasattr(request.user, 'profile'):
        return redirect('create_profile')

    return render(request, 'profile.html')
def network(request):
    return render(request, 'network.html')

def notification(request):

    jobs = Job.objects.order_by('-id')[:5]

    return render(request, 'notification.html', {'jobs': jobs})

@login_required
def message(request):

    messages_list = Message.objects.filter(receiver=request.user).order_by('-created_at')

    messages.success(request, "New connection request received")

    return render(request, 'message.html', {
        'messages_list': messages_list
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def signup(request):
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def register_view(request):
    return render(request, 'register.html')

@login_required
def send_message(request, user_id):

    receiver = User.objects.get(id=user_id)

    if request.method == "POST":

        text = request.POST.get("text")

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            text=text
        )

        messages.success(request, "Message sent successfully!")

        return redirect("message")

    return render(request, "send_message.html", {"receiver": receiver})


