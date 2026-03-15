
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    location = models.CharField(max_length=255, default='Unknown')  
    salary = models.IntegerField() 
    created_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="jobs_created"
)


    def __str__(self):
        return self.title


class Application(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='applications')
        job = models.ForeignKey(Job, on_delete=models.CASCADE)
        
        resume = models.FileField(upload_to="resumes/")
        applied_at = models.DateTimeField(auto_now_add=True)

        class Meta:
             unique_together = ('user','job')


        def __str__(self):
            return f"{self.user.username} applied for {self.job.title}"

class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")

    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"