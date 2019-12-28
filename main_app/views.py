from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Phi:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

phis = [
  Phi('Lolo', 'tabby', 'foul little demon', 3),
  Phi('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Phi('Raven', 'black tripod', '3 legged phi', 4)
]

# Define the home view

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def phis_index(request):
  return render(request, 'phis/index.html', { 'phis': phis })