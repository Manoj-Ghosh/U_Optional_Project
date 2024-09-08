from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    #return HttpResponse("Hello World !")
    meetups = [
        {
            'title' : 'A First Meetups', 
            'location': 'Durgapur', 
            'slug': 'a-first-meetups'
            
         },

        {
            'title' : 'A Second Meetups',
            'location': 'Kolkata', 
            'slug': 'a-second-meetups'
            
        }

    ]
    return render(request, 'meetups/index.html', {
        'show_meetups' : True,
        'meetups' : meetups
        })