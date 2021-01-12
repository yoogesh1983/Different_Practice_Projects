from django.http import HttpResponse
from twmblog.models import StaticPath

WEBSITE = '/website'
API = '/api'

class BlogpostMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        result = '<div><h3>Sorry Your responce could not be processed at the moment!! Please try again later...<h3> <span>Exception Name: {}</span> <br> <span>Reason: {}</span></div>'
        return HttpResponse(result.format(exception.__class__.__name__, exception))

    def process_template_response(self, request, response):
        url = request.get_full_path()
        if API not in url:
            response.context_data["userAuthenticated"] = request.user.is_authenticated
        if WEBSITE in url:
            path = url.rsplit('/', 1)[-1]
            if len(path) > 0:
                try:
                    static_path = StaticPath.objects.get(name=path)
                except StaticPath.DoesNotExist as msg:
                    path = 'NotFound'
                except Exception as msg:
                    path = 'Exception'
                else:
                    path = static_path.url
                response.context_data["staticBasePath"] = path
        return response
