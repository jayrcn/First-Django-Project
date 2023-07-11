#A view is a function that returns output to the browser interacting with the site 
#views for an application is stored in the view.py file inside the application's folder
from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

def index(request):
    return HttpResponse("Hello, world! This is the homepage of my website.")


def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book} ) #render function:  the process of transforming or translating or turning codes like html, css or Java codes, 
    #into interactive pages a website visitor can see or sees when they click on a link or reference link.
     
    # first to display (intially before the asethic change of displaying info) return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")
    #Now re-write the function to use the RENDER built-in in Django to take tge template and render it with 
    # the data we are passing in (the book object that we have looked up)






#Each var that is harvested from the URL is passed along to the function associted with it (book_id)


#The we use the book object we've created in models.py to look up the book by way of ID and use the ID to 
# return data about it to the user
