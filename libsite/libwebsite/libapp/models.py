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
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	@property	
	def checked_out(self):
		last_checkout = self.liblists.last()
		if last_checkout:
			return last_checkout.checked_out
		else:
			return False
	
	@property
	def is_overdue(self):
		if self.due_back and date.today() > self.due_back:
			return True
		return False

	def __str__(self):
			return self.title

class Liblist(models.Model):
#take list out of the name lullz
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='liblists')
# ForeignKey: book (is this just book status? this ain't checkout status tbh
	member = models.ForeignKey(User, on_delete=models.CASCADE)
# foreignkey: we need to instantiate a userclass
	checked_out = models.BooleanField(default=True)
#true means the book  is NOT checked out yet
	date = models.DateTimeField(default=datetime.now())

	def toggle_checkout(self):
		self.checked_out = not self.checked_out

	def __str__(self):
		return 'Book: '+str(self.book)+', Member: '+str(self.member)+', Checked Out: '+str(self.checked_out)+', Date: '+str(self.date)
# checkout: models.Boolean