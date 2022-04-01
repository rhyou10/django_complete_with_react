from email import message
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

post_list = ListView.as_view(model = Post) #클래스 기반 뷰

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '') #url에서 post_list 함수를 호출시 해당 url에서 GET 해라 'q'라는 인자를 반환 # 'q' 가 없을시 '' 반환 (검색어저장)
    
#     if q:
#         qs = qs.filter(message__icontains= q)

#     #instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list' : qs,
#         'q':q,

#     })

#아래 : --> type형태에 대한 hint의 라고 보면된다. 타입틀려도 eror x
def post_detail(request:HttpRequest, pk : int) -> HttpResponse:  
    
    response = HttpResponse()
    response.write("Hello world")
    return response

# Create your views here.
