from django.db import models

# Create your models here.
class PostsRate(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    rates = models.OneToOneField(PostsRate, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
