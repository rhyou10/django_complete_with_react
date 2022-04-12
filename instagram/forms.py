from django import forms
from .models import Post

#모델폼과 일반폼 차이점
#일반 폼은 폼 자체에서 데이터 받는 검증 형식 지정해야한다.
#모델 폼은 모델에 정의되어있는 검증 맞게 데이터 받는다.

class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'message', 'photo', 'tag_set', 'is_public'
        ]

