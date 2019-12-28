from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Phi

class PhiCreate(CreateView):
  model = Phi
  fields = '__all__'

class PhiUpdate(UpdateView):
  model = Phi
  fields = ['breed', 'description', 'age']

class PhiDelete(DeleteView):
  model = Phi
  success_url = '/phis/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def phis_index(request):
  phis = Phi.objects.all()
  return render(request, 'phis/index.html', { 'phis': phis })

def phis_detail(request, phi_id):
  phi = Phi.objects.get(id=phi_id)
  return render(request, 'phis/detail.html', { 'phi': phi })