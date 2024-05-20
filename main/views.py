from django.shortcuts import render
from .models import *

# Create your views here.
def about(request):
    return render(request,'main/aboutus.html')

def prayer(request):
    return render(request,'main/prayer.html')

def index(request):
    # Fetch attachments from all models
    attachments = []

    # Pastors
    pastors = Pastor.objects.filter(profile_pic__isnull=False).values('profile_pic', 'created_at')
    for pastor in pastors:
        attachments.append({
            'type': 'Pastor',
            'file': pastor['profile_pic'],
            'created_at': pastor['created_at']
        })

    # Sermons
    sermons = Sermon.objects.filter(attachment__isnull=False).values('attachment', 'created_at')
    for sermon in sermons:
        attachments.append({
            'type': 'Sermon',
            'file': sermon['attachment'],
            'created_at': sermon['created_at']
        })

    # Events
    events = Event.objects.filter(attachment__isnull=False).values('attachment', 'created_at')
    for event in events:
        attachments.append({
            'type': 'Event',
            'file': event['attachment'],
            'created_at': event['created_at']
        })

    # Causes
    causes = Cause.objects.filter(attachment__isnull=False).values('attachment', 'created_at')
    for cause in causes:
        attachments.append({
            'type': 'Cause',
            'file': cause['attachment'],
            'created_at': cause['created_at']
        })

    # Blogs
    blogs = Blog.objects.filter(attachment__isnull=False).values('attachment', 'created_at')
    for blog in blogs:
        attachments.append({
            'type': 'Blog',
            'file': blog['attachment'],
            'created_at': blog['created_at']
        })

    # Gallery
    galleries = Gallery.objects.filter(attachment__isnull=False).values('attachment', 'created_at')
    for gallery in galleries:
        attachments.append({
            'type': 'Gallery',
            'file': gallery['attachment'],
            'created_at': gallery['created_at']
        })

    # Sort attachments by created_at
    attachments = sorted(attachments, key=lambda x: x['created_at'], reverse=True)

    return render(request, 'main/index.html', {'attachments': attachments})