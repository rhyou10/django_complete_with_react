from django.contrib import admin
from .models import Post

#admin.site.register(Post) #모델등록 첫번쨰 방법

''' 모델등록 두번째 방법
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
'''

#모델등록 세번째 방법
@admin.register(Post) #wrapping
class PostAdmin(admin.ModelAdmin):
    list_display =['pk', 'message', 'message_length', 'is_public' ,'created_at', 'updated_at'] #모델에서 정의된 필드들 함수들을 넣을수 있다. admin 페이지에서 확인가능
    list_display_links = ['message'] #message를 통해 해당 Post로 들어갈수 있게한다(여러개 설정가능)

    list_filter = ['created_at', 'is_public'] # admin/ instagrm Post 모델에 오른쪽에 filter를 확인가능(시간순으로)   / filter가 여러개인경우 and 조건으로 보여준다.

    search_fields = ['message'] #admin page에서 Post 찾을때 검색을 message 기준으로

    def message_length(self, post):
        return len(post.message)