from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import EmployeeCreate, GeeksCreate, EmployeeList, EmployeeDetail, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    path('home/', views.home, name='home'),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path('showform/', views.showform, name='showform'),
    path('getform/', views.getform, name='getform'),
    #path('dishes/<str:dish>', views.menuitems, name='dishes'),
    re_path(r'^dishes/(\w+)/$', views.menuitems, name='dishes'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu_card/', views.menu_by_id, name='menu_id'),
    path('book/', views.book, name='book'),
    path('form/', views.form_view, name='form_view'),
    path('hello/<name>/', views.hello, name='hello'),
    path('index/', views.index, name='index'),
    path('filter/', views.filterview, name='filter'),
    path('new_form/', views.form_view, name='new_form'),
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'),  
    path('create/', EmployeeCreate.as_view(), name='EmployeeCreate'),
    path('geek/', GeeksCreate.as_view()),
    path('employees/success/', views.register),
    path('employees/list/', EmployeeList.as_view()),
    path('employees/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name = 'EmployeeDelete'), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

""" 'str': Matches any non-empty string consisting of any character except a slash ('/'). This is the default converter if no other converter is specified.
Example: path('category/<str:slug>/', views.category_detail)

'int': Matches an integer value.
Example: path('post/<int:pk>/', views.post_detail)

'slug': Matches a string consisting of ASCII letters, numbers, hyphens, or underscores, used for human-readable URLs.
Example: path('article/<slug:slug>/', views.article_detail)

'uuid': Matches a universally unique identifier (UUID) in either hyphenated or non-hyphenated format.
Example: path('profile/<uuid:user_id>/', views.profile_detail)

'path': Matches any non-empty string consisting of any character, including a slash ('/'). This converter is useful for capturing an entire URL path segment.
Example: path('page/<path:url_path>/', views.page_detail)

'str': Matches any non-empty string consisting of any character except a slash ('/'). This is the same as the default converter mentioned earlier.
Example: path('search/<str:query>/', views.search_results)"""