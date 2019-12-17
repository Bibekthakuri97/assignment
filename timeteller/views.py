from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    #return HttpResponse('hello')
    return render(request, 'timeteller\greeting.html')

def today(request):
    return render(request, 'timeteller/today.html')

def timestamp(request):
    return render(request, 'timeteller/timestamp.html')
