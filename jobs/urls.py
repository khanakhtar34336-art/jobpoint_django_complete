from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('add-job/', views.add_job, name='add_job'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/', views.job_list, name='job_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  # 👈 ye add karo
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('feed/', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('network/', views.network, name='network'),
    path('notification/', views.notification, name='notification'),
    path('message/', views.message, name='message'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('send-message/<int:user_id>/', views.send_message, name='send_message'),

]
