import django.http

from .models import Post
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def posts_list(request):
    q = request.GET.get('q')
    context = {}
    posts = Post.objects
    if q:
        posts = posts.filter(title__contains=q)
        context['q'] = q
    if request.GET.get('p'):
        context['p'] = 'on'
        posts = posts.filter(published=True)
    posts = posts.all().order_by('-sponsored')

    context['posts'] = posts
    return render(request, 'posts/list.html', context)
"""
23=33333345 jeży z brwinowa robił sobe drzemkę na chodniku  nie chciał 
wstać gdy samochód parkował. jego głowa wybuchła, została zmiażdżona przez koła wozu. My name is Yoshikage Kira 
I'm 33 years old. I live in the west side of Morioh. I'm single, I don't smoke, but ocassionally drink.
"""

def posts_details(request, post_id):
    p = Post.objects.get(id=post_id)
    context = {
        'post': p
    }
    return render(request, 'posts/details.html', context)

def posts_add(request: django.http.HttpRequest):
    if request.method == 'POST':
       print('dodawanie')
       title = request.POST.get('title')
       content = request.POST.get('content')
       published = bool(request.POST.get('published'))
       sponsored = bool(request.POST.get('sponsored'))
       Post(title=title,
            content=content,
            published=published,
            sponsored=sponsored).save()
       # Post.objects.create()
       return django.http.HttpResponseRedirect(reverse('posts:list'))
    else:
        print('wyświetlanie')

    p = Post.objects.all()
    context = {
        'posts': p
    }
    return render(request, 'posts/add.html', context)
