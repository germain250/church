from .models import *


def word_of_god(request):
    words = Word.objects.all()
    blogs = Blog.objects.order_by('-created_at')[:3]

    church = ChurchState.objects.all()

    return {'words_of_god': words,'blogs':blogs,'church_status':church}