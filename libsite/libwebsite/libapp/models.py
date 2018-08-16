import datetime
from django.db import models

url = models.CharField(max_length=100, unique=True)

class Author(models.Model):
	name = models.CharField(max_length=25, unique= True)

	pass
	def __str__(self):
		return self

class Book(models.Model):
		
	title = models.CharField(max_length=250, unique=True)
	pub_date = models.DateTimeField()
	author = models.ForeignKey(Author, on_delete='models.CASCADE')
	def __str__(self):
			return self
