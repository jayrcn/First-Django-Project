from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id') #add a route that takes in some data by way of URL
    #In this case the ID of the book we are looking for, the look up the book and return its details in a webpage
    
    #The item in "<>" is the variable retrived from that part of the URL (in this case its an integer)
]

#A URL pattren mpas a view function to a URL so 
#the function (shown above) is triggered when someone goes to that URL 
#The URLs for the app is stored in urls.py