from django import forms
from .models import Post
import re

#모델폼과 일반폼 차이점
#일반 폼은 폼 자체에서 데이터 받는 검증 형식 지정해야한다.
#모델 폼은 모델에 정의되어있는 검증 맞게 데이터 받는다.

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'message', 'photo', 'tag_set', 'is_public'
        ] #이것만하면 문제점 여기서는 작성자를 지정하지않아서

    def clean_message(self):# 유효성검사시 자동으로 실행된다. / clean_필드명으로 필드에 유효성검사
        message = self.cleaned_data.get('message')
        # if message:
        #     message = re.sub('[a-zA-z]', '', message)
        
        return message

