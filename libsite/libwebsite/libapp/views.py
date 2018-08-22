from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Liblist

def index(request):
    # sub in models for libraries
    probablybooks = Book.objects.all() 
    return render(request, 'libwebsite/index.html', {'books':probablybooks})

#assign the book to a user if there are no issues (manage issues as they come)
def checkinout(request, bookpk): 
    book = get_object_or_404(Book, pk=bookpk)
    if book.checked_out:
        last_checkout = Liblist.objects.filter(book=book).order_by('date').last()
        #member needs to be the latest
        member = last_checkout.member
        print(last_checkout, member)
        if request.user == member:
        #create a new entry to liblist for checking the book back in
            check_in = Liblist(book=book,member=request.user, checked_out=False)
            check_in.save()
        else: #say the book is checked out by somebody else
            #make it display a clone template that says a "nah can't do?"
            pass
    else: #should we just let the user take the book out? 
        pass
        


    # if checked_out.last_checkout is true check out        
    # if member.last_checkout != null, check out      


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