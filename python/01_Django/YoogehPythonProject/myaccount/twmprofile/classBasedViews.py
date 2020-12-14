from django.http import HttpResponse
from django.views.generic.base import View, TemplateView


class HelloworldView(View):
    def get(self, request):
        return HttpResponse('<h1>This is from class based view</h1>')

class HelloworldTemplateView(TemplateView):
    template_name = 'twmprofile/classBasedViews/results.html'

