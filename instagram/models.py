from distutils.command.upload import upload
#from email import message
from django.db import models
#from django.contrib.auth.models import User #굉장히 딱딱한 방식
from django.conf import settings #user import의 다른 방식
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d') #upload setting에 설정된 media 안에 저장폴더 상세설정(너무많은 media 파일들을 관리하기위하여)
                                                                             # 이때 저장장소를 함수로 설정할경우(문자열로 반환) 파일명을 원하는 것으로 변경 가능
    tag_set = models.ManyToManyField('Tag', blank=True) #다대 다인경우 blank가 필요할수 있다.
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # 자바 toString

    def __str__(self): # admin에서 class -> list_display 설정하여 보이지 않는다
        #return f"Custom Post objects ({self.id}) " 
        return f"{self.pk} : {self.message}"

    def get_absolute_url(self): # url-reverse위한 필수
        return reverse('instagram:post_detail', args=[self.pk])

    class Meta: # 기본정렬 default 정렬
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메시지 글자수" ## admin에서 display_list 할경우 colunm 이름 변경


class Comment(models.Model):  # 1 : N ForeingKey의 경우 N에 명시하면 된다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE ## 실제로는 post_id 필드가 db에 생성된다
                            ,limit_choices_to={'is_public':True}) # is_public :True인것만 연결하겠다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #post_set = models.ManyToManyField(Post)

    def __str__(self) :
        return self.name
