from django.shortcuts import render
from .models import Phi

# DEFINE BELLOW
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def phis_index(request):
  phis = Phi.objects.all()
  return render(request, 'phis/index.html', { 'phis': phis })

def phis_details(request):
  phis = Phi.objects.get(id=cat_id)
  return render(request, 'phis/index.html', { 'phis': phis })