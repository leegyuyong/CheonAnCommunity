import re

def coerce_to_post(request):
    if hasattr(request, 'is_coerced'):
        return
    if request.method == 'PUT' or request.method == 'DELETE':
        method = request.method
        if hasattr(request, '_post'):
            del request._post
            del request._files
        try:
            request.method = 'POST'
            request._load_post_and_files()
            request.method = method
        except AttributeError:
            request.META['REQUEST_METHOD'] = 'POST'
            request._load_post_and_files()
            request.META['REQUEST_METHOD'] = method
        if request.method == 'PUT':
            request.PUT = request.POST
        elif request.method == 'DELETE':
            request.DELETE = request.POST
        request.is_coerced = True

def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext