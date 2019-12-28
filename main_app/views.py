from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Phi



# DEFINE BELOW
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

class PhiCreate(CreateView):
  model = Phi
  fields = '__all__'
  success_url = '/phis/'