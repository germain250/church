from .models import *


def word_of_god(request):
    words = Word.objects.all()
    blogs = Blog.objects.order_by('-created_at')[:3]
    pastors = Pastor.objects.all()
    recent_sermon = Sermon.objects.order_by('-created_at').first()
    recent_event = Event.objects.order_by('-created_at').first()
    church = ChurchState.objects.all()
    events = Event.objects.order_by('-created_at')[:3]
    causes = Cause.objects.order_by('-created_at')[:3]
    sermons = Sermon.objects.order_by('-created_at')[:3]
    galleries = Gallery.objects.all()

    

    return {
        'words_of_god': words,
        'blogs':blogs,
        'church_status':church,
        'pastors':pastors,
        'recent_sermon':recent_sermon,
        'recent_event':recent_event,
        'events':events,
        'causes':causes,
        'files':galleries,
        'sermons':sermons,
        }