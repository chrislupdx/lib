from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

url = models.CharField(max_length=100, unique=True)

class Author(models.Model):
	name = models.CharField(max_length=25, unique= True)

	pass
	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=250, unique=True)
	pub_date = models.DateTimeField()
	author = models.ForeignKey(Author, on_delete='models.CASCADE')
	def __str__(self):
			return self.title

class Liblist(models.Model):
	book = models.ForeignKey(Book, on_delete='models.CASCADE')
# ForeignKey: book (is this just book status? this ain't checkout status tbh
	member = models.ForeignKey(User, on_delete='models.CASCADE')
# foreignkey: we need to instantiate a userclass
	bookcheckoutstatus = models.BooleanField(default=True)
#true means the book  is NOT checked out yet
	date = models.DateTimeField(default=datetime.now())

# checkout: models.Boolean