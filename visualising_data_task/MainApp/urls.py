from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('view-data/<str:data>/', views.ViewData.as_view(), name='view_data'),
]
