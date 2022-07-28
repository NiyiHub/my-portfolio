from django.db import models

class Project(models.Model):
	image					= models.ImageField(upload_to='images/')
	description				= models.CharField(max_length=200)
