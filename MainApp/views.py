from django.views import View
from django.shortcuts import render
from .models import Drink, Sweet
from .utils import RenderHTMLData

# Create your views here.


class HomePageView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class ViewData(View):
    template_name = 'data/view_data.html'

    def get(self, request, data):
        if data == 'drink':
            drink_data = RenderHTMLData(Drink)
            bar = drink_data.render('Drink')
            data = 'Drink'
        elif data == 'sweet':
            sweet_data = RenderHTMLData(Sweet)
            bar = sweet_data.render('Sweet')
            data = 'Sweet'
        else:
            data = None

        context = {
            'bar': bar,
            'data': data
        }
        return render(request, self.template_name, context)
