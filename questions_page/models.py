from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


def upload_gallery_image(instance, filename):
    return f"images/{instance.question.name}/gallery/{filename}"


class Image(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="images")
    image= models.FileField(upload_to ='images/') 


        