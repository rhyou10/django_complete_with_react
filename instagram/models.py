from distutils.command.upload import upload
from email import message
from django.db import models

class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d') #upload setting에 설정된 media 안에 저장폴더 상세설정(너무많은 media 파일들을 관리하기위하여)
                                                                             # 이때 저장장소를 함수로 설정할경우(문자열로 반환) 파일명을 원하는 것으로 변경 가능
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    # 자바 toString

    def __str__(self): # admin에서 class -> list_display 설정하여 보이지 않는다
        #return f"Custom Post objects ({self.id}) " 
        return f"{self.pk} : {self.message}"

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메시지 글자수" ## admin에서 display_list 할경우 colunm 이름 변경