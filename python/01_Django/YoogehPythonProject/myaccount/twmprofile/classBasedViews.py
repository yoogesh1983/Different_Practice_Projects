from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View, TemplateView

from twmprofile.models import Profile


class HelloworldView(View):
    def get(self, request):
        return HttpResponse('<h1>This is from class based view</h1>')


class HelloworldTemplateView(TemplateView):
    template_name = 'twmprofile/classBasedViews/templateView.html'


class HelloworldContextTemplateView(TemplateView):
    template_name = 'twmprofile/classBasedViews/contextView.html'
    #for class based views, if the context parameter are required, then this function will get called by django
    # *kwargs means any number of arguments you can pass whereas **kwargs means any number of key-value dictionary you can pass
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['firstName'] = 'Yoogesh'
        return ctx


#CRUD based views using Class based views
#####################################################
class ProfileListView(ListView):
    model=Profile
    #default template: profile_list.html i.e. LowerCaseofthemodel_list.html
    #default conext object: profile_list i.e. Lowercaseofmodel_list

    #This is optional as this will be the default used by django. however if you want to provide your own then you can use this approach
    template_name = 'twmprofile/profile_list.html'
    context_object_name = 'profile_list'

class ProfileDetailView(DetailView):
    model = Profile
    #default template: profile_detail.html i.e. LowerCaseofthemodel_list.html
    #default conext object: profile i.e. Lowercaseofmodel_list

    #This is optional as this will be the default used by django. however if you want to provide your own then you can use this approach
    template_name = 'twmprofile/profile_detail.html'
    context_object_name = 'profile'

class CreateProfileView(CreateView):
    model = Profile
    #fields = ('username', 'password', 'firstName', 'lastName', 'age')
    fields = '__all__'
    #default template: profile_form.html
    #default_context_object: There will be no context in this view

    #This is optional as this will be the default used by django. however if you want to provide your own then you can use this approach
    template_name = 'twmprofile/profile_form.html'

    # Besides this, You must provide a method "get_absolute_url(self)" in a model.py and here you should give a reverse URL that tells where do you want to redirect after successful insertion

class UpdateProrofileView(UpdateView):
    model = Profile
    fields = ('username', 'firstName', 'lastName', 'age')
    # default template: profile_form.html
    # default_context_object: There will be no context in this view

    # Besides this, You must provide a method "get_absolute_url(self)" in a model.py and here you should give a reverse URL that tells where do you want to redirect after successful updation

class DeleteProrofileView(DeleteView):
    model = Profile
    success_url = reverse_lazy('profiles')

    # This is optional as this will be the default used by django. however if you want to provide your own then you can use this approach
    # default template: profile_confirm_delete.html
    # default_context_object: profile

