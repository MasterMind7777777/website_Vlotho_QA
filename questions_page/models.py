from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Answer(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        

class Image(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="images")
    image = models.FileField(upload_to ='images/') 

class MediaFile(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="media_files")
    media_file = models.FileField(upload_to ='media/') 

        
