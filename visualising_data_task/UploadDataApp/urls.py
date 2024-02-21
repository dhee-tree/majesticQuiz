from django.urls import path
from . import views
from .forms import UploadDataForm

urlpatterns = [
    path('upload/', views.UploadDataView.as_view(form=UploadDataForm), name='upload_data'),
]
