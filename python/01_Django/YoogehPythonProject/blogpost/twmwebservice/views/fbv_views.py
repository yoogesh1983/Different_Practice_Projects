from django.http import JsonResponse


##################################################################################
# By using Function Based View
##################################################################################
def get_post_by_using_function_based_view(request):
    # This is dictionary
    dict_data = {'title': 'This is title', 'body': 'This is body', }

    # we need to convert dictionary into Json by using dumps() method
    # json_data = json.dumps(dict_data)
    # return HttpResponse(json_data, content_type='application/json')

    # Or you can use this method which does above tasks by this single line
    return JsonResponse(dict_data)