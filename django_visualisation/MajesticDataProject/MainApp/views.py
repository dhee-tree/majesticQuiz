from django.views import View
from django.shortcuts import render
from .utils import DataVisualisation
from .data import sweet_data, drink_data

# Create your views here.


class HomePageView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class ViewData(View):
    template_name = 'data/view_data.html'

    def get(self, request, data):
        if data == 'sweet':
            data_vis = DataVisualisation(sweet_data, 'Sweets', 'Amount', 'Sweet Data')
            data_vis.plot_data('sweet_data.png')
            filename = 'sweet_data.png'
        elif data == 'drink':
            data_vis = DataVisualisation(drink_data, 'Drinks', 'Amount', 'Drink Data')
            data_vis.plot_data('drink_data.png')
            filename = 'drink_data.png'
        else:
            return render(request, '404.html')

        context = {
            'file': filename,
        }
        return render(request, self.template_name, context)
