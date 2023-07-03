from django.contrib import admin
from .models import MenuCategory, Menu, Customer, Logger
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Person, Reservation

# Register your models here.

admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(Logger)
#admin.site.register(Person)
admin.site.unregister(User)
admin.site.register(Reservation)

@admin.register(User)
class NewAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True
        
        return form

@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name") 
    search_fields = ("last_name__startswith", )