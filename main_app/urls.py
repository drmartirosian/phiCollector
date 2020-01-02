from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('phis/', views.phis_index, name='index'),
  path('phis/<int:phi_id>/', views.phis_detail, name='detail'),
  path('phis/create/', views.PhiCreate.as_view(), name='phis_create'),
  path('phis/<int:pk>/update/', views.PhiUpdate.as_view(), name='phis_update'),
  path('phis/<int:pk>/delete/', views.PhiDelete.as_view(), name='phis_delete'),
  path('phis/<int:phi_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  # associate a toy with a phi (M:M)
  path('phis/<int:phi_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  # unassociate a toy and phi
  path('phis/<int:phi_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
  path('phis/<int:phi_id>/add_photo/', views.add_photo, name='add_photo'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
]