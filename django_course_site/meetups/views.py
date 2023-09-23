from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm

def index(request):
    # return HttpResponse('Hello world')
    # meetups = [
    #     { 'title': 'A First Meetup', 'location': 'New York', 'slug': 'a-first-meetup', 'slug': 'a-first-meetup' },
    #     { 'title': 'A Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup', 'slug': 'a-second-meetup' },
    # ]
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
        'show_meetups': True,
        # 'show_meetups': False,
    })

def meetup_details(request, meetup_slug):
    # selected_meetup = {
    #     'title': 'A First Meetup',
    #     'description': 'This is the first meetup!',
    # }
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant = registration_form.save()
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            # 'meetup_title': selected_meetup.title,
            # 'meetup_description': selected_meetup.description,
            'meetup': selected_meetup,
            'form': registration_form,
        })
    except Exception as exc:
        print(exc)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False,
        })
    

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'meetup_organizer': meetup.organizer_email,
    })