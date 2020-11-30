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

    if(request.method == 'POST'):
        # handling form submission scenario
        form = forms.SignupRequest(request.POST)
        if form.is_valid():
            print("Form validation success", form.cleaned_data)
            ctx = {'name': form.cleaned_data['firstName']}
            form = forms.SignupRequest()
            return render(request, 'twmprofile/thankyou.html', ctx)
        else:
            ctx = {'today': datetime.datetime.now(), 'profiles': profiles, 'form': form}
            return render(request, 'twmprofile/wish.html', context=ctx)

    elif (request.method == 'GET'):
        form = forms.SignupRequest()
        ctx = {'today' : datetime.datetime.now(), 'profiles': profiles, 'form': form}
        return render(request, 'twmprofile/wish.html', context=ctx)

    return render(request, 'twmprofile/wish.html')