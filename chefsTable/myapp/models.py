from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.menu_category_name

class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")
    price = models.IntegerField()

    #def __str__(self):
    #    return self.menu_item + " : " + self.category_id
    def __str__(self) -> str:
        return self.menu_item
    
class Menuitems(models.Model):
    itemname = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name

class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time = models.TimeField(help_text="Enter the exact time")

class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField()

    def __str__(self):
        return (f"{self.first_name}, {self.last_name}")

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number', max_length=300)
    booking_time = models.DateTimeField(auto_now=True)
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return (f"{self.name}, {self.contact}, {self.notes}")

class Employee(models.Model):   
    name = models.CharField(max_length=100)   
    email = models.EmailField()   
    contact = models.CharField(max_length=15) 

class GeeksModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title  
    