class ExecutionFlowMiddleware(object):
    def __init__(self, get_response):
        print('init() method is called...')
        self.get_response = get_response

    def __call__(self, request):
        print('Request is called...')
        response = self.get_response(request)
        print('Response is called...')
        return response
