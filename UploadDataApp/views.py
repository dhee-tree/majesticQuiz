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

    def post(self, request, *args, **kwargs):
        post_form = self.form(request.POST, request.FILES)

        if post_form.is_valid():
            uploaded_file = post_form.cleaned_data['file']

            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)

            saved_file = fs.path(filename)

            try:
                renderfile = RenderUploadFileHTML(saved_file)
                bar = renderfile.render()

                messages.success(request, 'File uploaded successfully')

                context = {
                    'form': self.form,
                    'bar': bar,
                }

                return render(request, self.template_name, context)
            except ValueError as e:
                messages.error(request, e)
                return render(request, self.template_name, {'form': self.form})
        else:
            messages.error(request, 'File upload failed. Please try again')
            return render(request, self.template_name, {'form': self.form})
