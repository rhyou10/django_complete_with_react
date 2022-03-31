from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe # 안전하다는것을 표시하여 이미지로 표시될수있다.

#admin.site.register(Post) #모델등록 첫번쨰 방법

''' 모델등록 두번째 방법
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
'''

#모델등록 세번째 방법
@admin.register(Post) #wrapping
class PostAdmin(admin.ModelAdmin):
    list_display =['id', 'photo_tag', 'message', 'message_length', 'is_public' ,'created_at', 'updated_at'] #모델에서 정의된 필드들 함수들을 넣을수 있다. admin 페이지에서 확인가능
    list_display_links = ['message'] #message를 통해 해당 Post로 들어갈수 있게한다(여러개 설정가능)

    list_filter = ['created_at', 'is_public'] # admin/ instagrm Post 모델에 오른쪽에 filter를 확인가능(시간순으로)   / filter가 여러개인경우 and 조건으로 보여준다.

    search_fields = ['message'] #admin page에서 Post 찾을때 검색을 message 기준으로


    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src = "{post.photo.url}" width = 75px/>') #mark_safe를 통해 안전하다고 하여 이미지로 표시할수있다. not text // post.photo.url 표현가능한이유는 사진이기떄문(path, url setting에 설정했기떄문)


    def message_length(self, post):
        return len(post.message)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass