from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/aboutus.html')

def prayer(request):
    return render(request,'main/prayer.html')