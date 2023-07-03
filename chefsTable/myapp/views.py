from django.shortcuts import render
from .forms import LogForm
from .models import Menu, Employee, GeeksModel

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView 

def home(request):
    #greeting = "<h1>Welcome to Little Lemon!</h1>"
    #return HttpResponse(greeting)
    return render(request, "home.html", {})

def register(request): 
    return render(request, "register.html", {}) 

def login(request): 
    return render(request, "login.html", {}) 

def pathview(request, name, id):
    return HttpResponse("Name:{} <br>UserID:{}".format(name, id))

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name: {} <br>UserID: {}".format(name,id))

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse("Name: {} <br>UserID: {}".format(name, id))

def menuitems(request, dish):
    items = {
        'pasta' : 'Pasta is a type of noodle made from combination of wheat, water and eggs',
        'falafel' : 'Falafel are deep fried aptties or balls made from...',
        'cheesecake' : ' Cheesecake is a type of dessert made with cream...'
    }

    description = items[dish]

    return HttpResponse("<h2> {} </h2>".format(dish) + description)

def about(request):
    about_content = {
        'about': 'Based in Chicago, Illinois, Little Lemon is a family owned Mediterranean restaurant, focused on traditional recipes served with a modern twist.'
    }

    return render(request, "about.html", about_content)

def menu(request):
    newmenu = {
        'pasta' : '12',
        'falafel' : '10',
        'cheesecake' : '8',
    }
    return render(request, "menu.html", {'newmenu': newmenu})

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)

def book(request):
    return HttpResponse("<h2>Make a booking:</h2>")

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "new_form.html", context)

def index(request):#, name):
    #context = {"name": name}
    items = {
        'Pasta' : 'Pasta is a type of noodle made from combination of wheat, water and eggs',
        'Falafel' : 'Falafel are deep fried aptties or balls made from...',
        'Cheesecake' : ' Cheesecake is a type of dessert made with cream...'
    }
    return render(request, 'index.html', {'items':items})

def hello(request, name):
    context = {"name": name}
    return render(request, 'hello.html', context)

def filterview(request): 
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust']
    dct = {'digits': ['One', 'Two', 'Three'],'tens': ['Ten', 'Twenty', 'Thirty']} 
    return render(request, 'filter.html', {'langs':langs, 'dct': dct}) 

class EmployeeCreate(CreateView):   
    model = Employee    
    fields = '__all__' 
    success_url = "/employees/list/"
    template_name = "employee_form.html"

from django.views.generic.list import ListView  

class EmployeeList(ListView):   
    model = Employee
    template_name = "employee_list.html"

from django.views.generic.detail import DetailView

class EmployeeDetail(DetailView):
    model = Employee
    template_name = "employee_detail.html"

from django.views.generic.edit import UpdateView  

class EmployeeUpdate(UpdateView):   
    model = Employee   
    fields = '__all__'   
    success_url = "/employees/list/"
    template_name = "employee_update_form.html"

from django.views.generic.edit import DeleteView

class EmployeeDelete(DeleteView):   
    model = Employee   
    success_url = "/employees/list/"
    template_name = "employee_confirm_delete.html"

class GeeksCreate(CreateView):
    model=GeeksModel
    fields = ['title', 'description']
    template_name = "geeksmodel_form.html"
