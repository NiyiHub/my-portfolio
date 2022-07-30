from django.db import models
from django.db.models import Model

class Blog(models.Model):
	title						= models.CharField(max_length=255)
	pub_date					= models.DateTimeField(auto_now_add=True)
	body						= models.TextField(max_length=500)
	image						= models.ImageField(upload_to='Images/')
