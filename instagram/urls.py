from django.urls import path, re_path, register_converter
from . import views


class YearConverter():
    regex = r"20\d{2}" # 20으로 시작하며 정수 2번 반복

    def to_python(self, value):
        return int(value) #정수로 변환하여 넘긴다.

    def to_url(self, value):
        return str(value)

register_converter(YearConverter, 'year')## custom converter 만듬, 자주쓰는 url 패턴의경우 만든다.


app_name = "instagram" #안넣어도 구동가능, URL_REVERSE에서 namespace 역할을 하게된다.

urlpatterns=[
    path('', views.post_list),
    path('<int:pk>/',views.post_detail),#re_path(r'(?P<pk>\d+)/$', views.post_detail), #위와 같은의미

    path('archives/<year:year>/', views.archives_year),
    #path('archives/<int:year>/', views.archives_year),
    #re_path(r'archives/(?P<year>\d+)/', views.archives_year), #정규포현식을 사용 원하는 정확한 인자로 주소설정가능 (?P<year>\d+)

]