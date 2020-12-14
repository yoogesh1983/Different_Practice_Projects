from django.http import HttpResponse
from django.views.generic.base import View, TemplateView


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
