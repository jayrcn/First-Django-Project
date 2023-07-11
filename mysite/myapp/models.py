from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



# Create your models here.
#A model describes the database objects used in the site 
#such as the tables, the fields, etc

#This example will just have one table called "Book"
#This table has two fields, one for the name of the book and the other field is
#the publishing date
