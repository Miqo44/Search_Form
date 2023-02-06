from django.shortcuts import render
from .models import Post
from django.db.models import Q

def index(request):

    search_post = request.GET.get('search')

    if search_post:    
        posts = Post.objects.filter(Q(title__icontains=search_post) | Q(content__icontains=search_post))
    else:    
        posts = Post.objects.all().order_by("-date_created")
    return render(request, 'main/index.html', {'posts': posts})