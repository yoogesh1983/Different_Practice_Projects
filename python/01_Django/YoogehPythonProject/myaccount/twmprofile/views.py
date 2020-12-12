import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from twmprofile.models import Profile

from . import forms


def getProfile(request):
    redirecturl = 'twmprofile/wish.html'
    ctx = ''
    if request.method == 'POST':
        # handling form submission scenario
        form = forms.AdminSignupRequest(request.POST)
        if form.is_valid():
            print("Form validation success. Going to save data into Database", form.cleaned_data)
            ctx = {'name': form.cleaned_data['first_name'], 'title': 'Thank You'}

            # Saving into a database (You must set password after form.save to save the encrypted data into database)
            # Otherewise it will not work
            user = form.save(commit=True)
            user.set_password(user.password)
            user.save()

            form = forms.AdminSignupRequest()
            return HttpResponseRedirect('/accounts/login')
        else:
            ctx = {'today': datetime.datetime.now(), 'form': form }
            redirecturl = 'twmprofile/wish.html'

    elif request.method == 'GET':
        form = forms.AdminSignupRequest()
        ctx = {'today': datetime.datetime.now(), 'form': form}
        redirecturl = 'twmprofile/wish.html'

    response = render(request, redirecturl, ctx)
    return response






@login_required
def getJavaExamView(request):
    redirecturl = 'twmprofile/javaExam.html'
    ctx = ''
    if request.method == 'POST':
        # handling form submission scenario
        form = forms.AdminSignupRequest(request.POST)
        if form.is_valid():
            print("Form validation success. Going to save data into Database", form.cleaned_data)
            ctx = {'name': form.cleaned_data['first_name'], 'title': 'Thank You'}

            # Saving into a database (You must set password after form.save to save the encrypted data into database)
            # Otherewise it will not work
            user = form.save(commit=True)
            user.set_password(user.password)
            user.save()

            form = forms.AdminSignupRequest()
            return HttpResponseRedirect('/accounts/login')
        else:
            ctx = {'form': form}
            redirecturl = 'twmprofile/javaExam.html'
    else:
        form = forms.AdminSignupRequest()
        ctx = {'form': form}
        redirecturl = 'twmprofile/javaExam.html'

    return render(request, redirecturl, ctx)