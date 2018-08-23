from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Book, Liblist


def index(request):
    # sub in models for libraries
    probablybooks = Book.objects.all() 
    checked_out_books = None
    if request.user.is_authenticated:
        checked_out_books = Book.objects.filter(borrower=request.user)
    return render(request, 'libapp/index.html', {'books':probablybooks, 'borrowlist':checked_out_books})


#build aout a context that links  Liblist to index


#assign the book to a user if there are no issues (manage issues as they come)
@login_required
def checkinout(request, bookpk): 
    book = get_object_or_404(Book, pk=bookpk)
    if book.checked_out:
        #member needs to be the latest
        member = book.borrower
        if request.user == member:
        #create a new entry to liblist for checking the book back in
            check_in = Liblist(book=book,member=request.user, checked_out=False)
            check_in.save()
            book.borrower = None
            book.save()
        else:
            return render(request, 'libapp/nobookforyou.html')
    else:
        check_out = Liblist(book=book,member=request.user, checked_out=True)
        check_out.save()
        book.borrower = request.user
        book.save()
    return redirect('libapp:index')



#assign book to user 

#last_checkout is a cross-section of liblists as asserted by book, 
#we need to assign a book to a user 
    

#     book_on_table.liblist_set.order_by('-date')
#     entries_in_liblist = Liblist.objects.filter(book=book_on_table).order_by('-date')
#     print(entries_in_liblist)
#     if entries_in_liblist.exists():
#         entry = entries_in_liblist[0]
#         if Liblist.objects.filter(status=bookcheckoutstatus).exists(False):
#         #is the book on the checkout list?
#             return 404
#         if Liblist.objects.filter(member = member).exists():
#             return 404
#         else check out book
#     else:
#         some other logic
# oes book exist in libslit
#     if checkoutstatus in model returns true
#     if member in model returns true (as in member field isn't null) AND if the member is not x return 
        


# once connected, check if the title's entry in database for book checkoutstatus:
#if checked out, return fuck off, else check out
    return HttpResponse(bookpk)



#check-out view (post): takea  book out of the library and assign to user,take a book out of the library and put it in the user's checkout list
#check-in view (post): return a book to the library and take it off of the user's checkout list
#under a user's record list books they take out, add a book to the user's record


#figure out what andi how you need to wire it
#model connect
#template connect

#do check-in and check-out need unique and individual defs if they're both playing off of the same system?

# def with book data, lookup in db and see if it's available then fork yes/no 
# (yes for checkin)
# no for checkout