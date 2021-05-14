from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Profile
from django.contrib.auth.models import User


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request,'blog/blog_list.html', {'blogs': blogs})

def recent(request):
    blogs = Blog.objects.all()[:2]
    return render(request, 'blog/recent.html', {'blogs': blogs})


def blog_detail(request,slug):
    detail=get_object_or_404(Blog,pk=slug)
    return render(request,'blog/blog-detail.html',{'detail':detail})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)#get user,username or nothing(404 error)
    profile = Profile.objects.get(user=user) # get profile objects belonging to specific user

    return render(request,'blog/blog-profile.html',{'detail':profile})