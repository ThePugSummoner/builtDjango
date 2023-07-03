from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("<h1>404: Page not Found!</h1>")