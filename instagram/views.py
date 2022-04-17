from email import message
from http.client import HTTPResponse
from urllib import response
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import redirect, render,get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.contrib.auth.decorators import login_required # 장식자 호출
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import PostForm

# post_list = login_required(ListView.as_view(model = Post, paginate_by = 10)) #클래스 기반 뷰 아직 검색기능 미구현

# 새로운 포스트 생성
@login_required
def post_new(request): ##form 사용법
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # post = form.save(commit=True)#commit default : true / 인스턴스를 save 할것이냐 false일시 데이터 저장 안됨 / post.save가 생략될수 있다.
            # post = form.save(commit=False)
            # post.save()
            post = form.save(commit=False)# form에는 user가 생략되어있어서 사용
            post.author = request.user #현재 로그인 유저확인
            post.save() # user 받고 저장
            
            #message # 소비하는 코드는 layout.html
            messages.success(request, '포스팅을 저장하였습니다.')

            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'instagram/post_form.html', {
        'form':form,
        'post': None,        
    })

#Post 수정
@login_required #로그인 필요 장식자
def post_edit(request, pk):
    post = get_object_or_404(Post,pk=pk)

    # 작성자 check tip
    if post.author != request.user:
        messages.error(request, '작성자만 수정가능합니다.')
        return redirect(post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save() # 수정의경우 user가 이미 지정되어있어 commit default

            #message # 소비하는 코드는 layout.html
            messages.success(request, '포스팅을 수정하였습니다.')

            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request, 'instagram/post_form.html', {
        'form':form,
        'post': post,
    })


# 포스트 삭제
@login_required 
def post_delete(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method== 'POST':
        post.delete()
        messages.success(request, "포스팅을 삭제하였습니다.")
        return redirect('instagram:post_list')

    return render(request, 'instagram/post_confirm_delete.html',{
        'post':post
    })





#@method_decorator(login_required, name = 'dispatch')
class PostListView(LoginRequiredMixin ,ListView): # 장식자 로그인 접근방법과 상속을 통한 로그인 접속방법
    model = Post
    paginate_by = 100

post_list = PostListView.as_view(paginate_by=20)



# @login_required #로그인 여부, 안되어 있을시 로그인 페이지로 / 주소 defalut : accounts/login
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

# def archives_year(request, year):
#     return HttpResponse(f"{year} archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field = 'created_at', paginate_by =10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field = 'created_at', make_object_list = True)

