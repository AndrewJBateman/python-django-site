from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
  curDT = datetime.now()
  date_time = curDT.strftime("%m/%d/%Y, %H:%M:%S")
  return render(request, "aboutus/index.html", {"datetime":date_time});

def aboutus(request):
  return HttpResponse('<h1>This is about us</h1>')
