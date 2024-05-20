from django.db import models
from django.utils import timezone

def pastor_pic(instance,filename):
    return f"pastors/{filename}+{instance.name}"

def sermon_pic(instance,filename):
    return f"sermons/{filename}+{instance.title}"

def event_pic(instance,filename):
    return f"events/{filename}+{instance.title}"

def causes_file(instance,filename):
    return f"causes/{filename}+{instance.title}"

def blog_files(instance,filename):
    return f"blog_files/{filename}+{instance.title}"

def gallery(instance,filename):
    return f"gallery/{filename}+{instance.title}"

# Create your models here.

class Pastor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to=pastor_pic, blank=True, null=True)
    facebook = models.CharField(max_length=100,null=True,blank=True)
    instagram = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,max_length=100,null=True,blank=True,)
    
class Sermon(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,max_length=100,null=True,blank=True)
    updated_at = models.DateField(auto_now=True,max_length=100,null=True,blank=True)
    pastor = models.ForeignKey(Pastor,on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=sermon_pic, blank=True, null=True)
    
    
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(null=True, blank=True, upload_to=event_pic)
    
class Prayer(models.Model):
    name = models.CharField(max_length=100)
    prayer_request = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    
class Cause(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    attachment = models.FileField(max_length=100,null=True,blank=True,upload_to=causes_file)
    
class Blog(models.Model):
    author = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    attachment = models.FileField(max_length=100,null=True,blank=True,upload_to=blog_files)
    created_at = models.DateTimeField(auto_now_add=True,max_length=100,null=True,blank=True)
    
class Comment(models.Model):
    comment = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,max_length=100,null=True,blank=True)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    author = models.CharField(max_length=100,null=True,blank=True)
    

class Gallery(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    attachment = models.FileField(max_length=100,null=True,blank=True,upload_to=gallery)
    
class Word(models.Model):
    verse = models.CharField(max_length=30,null=True,blank=True)
    scripture = models.TextField(null=True,blank=True)
    
class ChurchState(models.Model):
    believers = models.IntegerField(null=True, blank=True)
    ministries = models.IntegerField(null=True, blank=True)
    pastors = models.IntegerField(null=True, blank=True)
    volunteers = models.IntegerField(null=True, blank=True)
    saved = models.IntegerField(null=True, blank=True)
    
    
    

