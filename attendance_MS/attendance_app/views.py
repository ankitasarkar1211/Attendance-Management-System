from django.shortcuts import render

def index(request):
  return render(request,'index.html')

def log_in(request):
  return render(request,'log_in.html')

