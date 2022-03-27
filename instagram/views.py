from email import message
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '') #url에서 post_list 함수를 호출시 해당 url에서 GET 해라 'q'라는 인자를 반환 # 'q' 가 없을시 '' 반환 (검색어저장)
    
    if q:
        qs = qs.filter(message__icontains= q)

    #instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list' : qs,
        'q':q,

    })

# Create your views here.
