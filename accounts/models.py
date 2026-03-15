from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import admin



class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name="posted_jobs")
    
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    about = models.TextField(blank=True)
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    graduation_year = models.IntegerField(null=True, blank=True)
    is_employer = models.BooleanField(default=False)   # ✅ NEW FIELD
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Connection(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connection_sender")

    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="connection_receiver")

    status = models.CharField(max_length=10, default="pending")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
