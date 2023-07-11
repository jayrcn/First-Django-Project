from django.contrib import admin

from .models import Book
admin.site.register(Book)

# Register your models here.
# Register the models (tables here in the admin file (aka Django admin system))

#This allows us to directly manage the table directly in the admin page for our Django project

#How to register a new model in the admin file?!!
#We just edit admin.py for the app and insert a reference to our newly created tables
#SEE EXAMPLE ABOVE
