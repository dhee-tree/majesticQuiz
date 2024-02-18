from django.views import View
from django.shortcuts import render

# Create your views here.


class HomePageView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)