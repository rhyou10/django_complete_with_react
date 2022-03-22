from django.shortcuts import render
from .models import Post
# Create your views here.

def PostList(request):
    qs = Post.objects.all() # Query set
    return render(request, 'blog1/post_list.html', {
        'post_list' : qs,

    })