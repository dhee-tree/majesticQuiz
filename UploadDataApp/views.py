from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .utils import RenderUploadFileHTML
from django.core.files.storage import FileSystemStorage

# Create your views here.

class UploadDataView(View):
    form = None
    template_name = 'data/upload_data.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})
        