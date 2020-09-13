from django.http import HttpResponse

def about(request):
    return HttpResponse('About')

def home(request):
    return HttpResponse('Home')