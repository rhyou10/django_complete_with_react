from email import message
from django.db import models

class Post(models.Model):
    message = models.TextField()
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