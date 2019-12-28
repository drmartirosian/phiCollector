from django.shortcuts import render
# Add the following import
from django.http import HttpResponse



# Create your views here.

#render => html file location, pass dictionary
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def phis_index(request):
  return render(request, 'phis/index.html', {
       'phis': phis
    })