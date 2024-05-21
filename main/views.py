from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
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
            messages.success(request, 'Prayer request added successfully')
            return redirect('index')
    else:
        form = PrayerForm()
    return render(request,'main/prayer.html',{'form':form})


def send_email(request):
    if request.method == 'POST':
        to_email = 'cgpt07949@gmail.com'
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if subject and email and message:
            try:
                full_subject = f"{subject} from {email}"
                formatted_message = f"Sender: {email}\n\nMessage:\n{message}"
                send_mail(full_subject, formatted_message, 'germainconnected@gmail.com', [to_email])
                messages.success(request, 'Email sent successfully')
                return redirect('index')
            except Exception as e:
                print(f"Error sending email: {e}")
                messages.error(request, 'Error sending email. Please try again later.')
        else:
            print("Missing subject, email, or message")
            messages.error(request, 'All fields are required.')
    return redirect('index')



