from django.http import HttpResponse

class CatchGlobalException(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):

        result = '<div><h3>Sorry Your responce could not be processed at the moment!! Please try again later...<h3> <span>Exception Name: {}</span> <br> <span>Reason: {}</span></div>'
        return HttpResponse(result.format(exception.__class__.__name__, exception))
