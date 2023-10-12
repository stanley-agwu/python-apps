from django.db import models

# Create your models here.
class Player(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	football_club=models.CharField(max_length=50)
	nationality=models.CharField(max_length=50)
	age=models.IntegerField()
	position=models.CharField(max_length=50)

	def __str__(self):
		return self.first_name + " " + self.last_name
