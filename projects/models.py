from django.db import models

class Project(models.Model):
	title					= models.CharField(max_length=200)
	image					= models.ImageField(upload_to='images/')
	description				= models.CharField(max_length=500)
	project_url				= models.URLField(max_length=200, null=True)

	def __str__(self):
		return self.title

	def summary(self):
		return self.description[:100]


