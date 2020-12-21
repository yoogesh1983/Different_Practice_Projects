import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import forms

"""
def getProfile(request):
    profiles = Profile.objects.all()

    redirecturl = 'twmprofile/home.html'
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
            redirecturl = 'twmprofile/home.html'

    elif request.method == 'GET':
        form = forms.SignupRequest()
        ctx = {'today': datetime.datetime.now(), 'profiles': profiles, 'form': form, 'title': 'Profile Information'}
        redirecturl = 'twmprofile/home.html'

    response = render(request, redirecturl, ctx)
    #response.set_cookie('count', int(request.COOKIES.get('count', 0)) + 1, max_age=180) # max_age is optonal
    response.set_cookie('count', int(request.COOKIES.get('count', 0)) + 1) # max_age is optonal

    return response

@login_required
def getAdminView(request):
    redirecturl = 'twmprofile/admin.html'
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
            redirecturl = 'twmprofile/admin.html'
    else:
        form = forms.AdminSignupRequest()
        ctx = {'form': form}
        redirecturl = 'twmprofile/admin.html'

    return render(request, redirecturl, ctx)


# Create
def InsertIntoProfiles(request):
    form = forms.SignupRequest(request.POST)
    form.save(commit=True)

# Read
def getAllProfiles(request):
    profiles = Profile.objects.all()
    # profiles = Profile.objects.filter(age__lt=35)
    # profiles=Profile.objects.filter(username__startswith='A')
    # profiles=Profile.objects.all().order_by('username')
    # profiles=Profile.objects.all().order_by('-age')

# update
def updateProfile(request, id):
    existingProfile = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ProfileUpdateRequest(request.POST, instance=existingProfile) # A record will be considered new if you do not provide instance=Profile
        print('Is form valid', form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/twmprofile/home')

    return render(request, 'twmprofile/update.html', {'profile': existingProfile})

# delete
def deleteProfile(request, id):
    print("Deleting profile with id", id)
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('/twmprofile/home')

"""