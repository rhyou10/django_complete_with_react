from email import message
from http.client import HTTPResponse
from urllib import response
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView

post_list = ListView.as_view(model = Post, paginate_by = 10) #클래스 기반 뷰 아직 검색기능 미구현

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

# def post_detail(request:HttpRequest, pk : int):# -> HttpResponse:
#     # try:
#     #     post = Post.objects.get(pk=pk) #url에서 받은 pk값과 일치하는 Post 가지고와라 # pk 없을시 DoesNotExits 에러발생한다.
#     # except Post.DoesNotExist:
#     #     raise Http404
#     post = get_object_or_404(Post, pk=pk) #위 try except를 간소화할수 있다.
  
#     return render(request, "instagram/post_detail.html",{
#         'post':post,
#     })
#     #response = HttpResponse()
#     #response.write("Hello world")
#     #return response
post_detail = DetailView.as_view(model=Post)

def archives_year(request, year):
    return HttpResponse(f"{year} archives")

