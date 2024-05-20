from django.shortcuts import render,redirect
from .form import PrayerForm

# Create your views here.

def index (request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/aboutus.html')

def prayer(request):
    return render(request,'main/prayer.html')

def save_prayer(request):
    if request.method == 'POST':
        form = PrayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PrayerForm()
    return render(request,'main/prayer.html',{'form':form})



