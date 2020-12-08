import datetime

from django.shortcuts import render
from twmprofile.models import Profile

from . import forms


def getProfile(request):
    profiles = Profile.objects.all()
    # profiles = Profile.objects.filter(age__lt=35)
    # profiles=Profile.objects.filter(username__startswith='A')
    # profiles=Profile.objects.all().order_by('username')
    # profiles=Profile.objects.all().order_by('-age')

    redirecturl = 'twmprofile/wish.html'
    ctx = ''

    if request.method == 'POST':
        # handling form submission scenario
        form = forms.SignupRequest(request.POST)
        if form.is_valid():
            print("Form validation success. Going to save data into Database", form.cleaned_data)
            ctx = {'name': form.cleaned_data['firstName'], 'title': 'Thank You'}

            # Saving into a database
            form.save(commit=True)

            form = forms.SignupRequest()
            redirecturl = 'twmprofile/thankyou.html'
        else:
            ctx = {'today': datetime.datetime.now(), 'profiles': profiles, 'form': form, 'title': 'Profile Information'}
            redirecturl = 'twmprofile/wish.html'

    elif request.method == 'GET':
        form = forms.SignupRequest()
        ctx = {'today': datetime.datetime.now(), 'profiles': profiles, 'form': form, 'title': 'Profile Information'}
        redirecturl = 'twmprofile/wish.html'

    response = render(request, redirecturl, ctx)
    #response.set_cookie('count', int(request.COOKIES.get('count', 0)) + 1, max_age=180) # max_age is optonal
    response.set_cookie('count', int(request.COOKIES.get('count', 0)) + 1) # max_age is optonal

    return response
