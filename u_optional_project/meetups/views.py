from django.shortcuts import render
from django.http import HttpResponse

from .models import Meetup 
from .forms import RegistrationForm
# Create your views here.


def index(request):
    #return HttpResponse("Hello World !")
    meetups = Meetup.objects.all()
    
    return render(request, 'meetups/index.html', {
        'show_meetups' : True,
        'meetups' : meetups
        })


def meetup_details(request, meetup_slug):

    try:
        selected_meetups = Meetup.objects.get(slug=meetup_slug)
        registration_form = RegistrationForm()
        return render(request, 'meetups/meetups-details.html', {
            'meetup_found':True,
            'meetup': selected_meetups,
            'form': registration_form
        })
    except Exception as exc:
        return render(request,'meetups/meetups-details.html',{
            'meetup_found':False
        } )
