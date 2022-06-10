from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime

def index(request):
    context = {
        "date": datetime.today().strftime('%b %d,  %Y'),
        "time": strftime("%H:%M %p",gmtime())
    }
    return render(request, 'index.html', context)

    




