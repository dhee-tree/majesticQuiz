from django.shortcuts import render


class Main505Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        from django.http import HttpResponseServerError

        if isinstance(exception, Exception):
            return render(request, '404.html', {}, status=404)

        return None
