from django.urls import path
from . import views

urlpatterns = [
    #url path, views def, name for templates
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('phis/', views.phis_index, name='index'),
    path('phis/<int:phi_id>/', views.phis_details, name='detail'),
    path('phis/create/', views.PhiCreate.as_view(), name='phis_create'),
]