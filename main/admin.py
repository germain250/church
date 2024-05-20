from django.contrib import admin
from .models import Pastor, Sermon, Event, Prayer, Cause, Blog, Comment, Gallery, Word, ChurchState

# Register your models here.

@admin.register(Pastor)
class PastorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'pastor')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    list_filter = ('start_date', 'end_date')

@admin.register(Prayer)
class PrayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'prayer_request', 'created_at')
    search_fields = ('name', 'prayer_request')
    list_filter = ('created_at',)

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at')
    search_fields = ('author', 'title', 'content')
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment', 'created_at', 'blog')
    search_fields = ('author', 'comment')
    list_filter = ('created_at',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('verse', 'scripture')
    search_fields = ('verse', 'scripture')
    
@admin.register(ChurchState)
class ChurchStateAdmin(admin.ModelAdmin):
    list_display = ('believers', 'ministries','volunteers','pastors')
    search_fields = ('pastors', 'believers', 'volunteers')

# Customize the admin site titles
admin.site.site_header = "Church Administration"
admin.site.site_title = "Church Administration"
admin.site.index_title = "Welcome to Church Administration"
