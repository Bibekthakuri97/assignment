from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    d = {
        'name': 'Back to Future! '  
        }

    #{{this is called jinja templating}}
    #{%this is to write codes in html%}
    #return HttpResponse('hello')
    return render(request, 'timeteller\greeting.html',d)

def today(request):
    todaysdate = datetime.datetime.today()

    d={
        'todaysdate': todaysdate
    }
    
    return render(request, 'timeteller/today.html',d)

def timestamp(request):
    todaystimestamp = datetime.datetime.timestamp()

    d={
        'todaystimestamp': todaystimestamp
    }
    
    return render(request, 'timeteller/timestamp.html',d)
