from django.urls import path, re_path, register_converter
from . import views
from .converters import YearConverter, MonthConverter, DayConverter



register_converter(YearConverter, 'year')## custom converter 만듬, 자주쓰는 url 패턴의경우 만든다.
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = "instagram" #안넣어도 구동가능, URL_REVERSE에서 namespace 역할을 하게된다.

urlpatterns=[
    path('new/', views.post_new, name='post_new' ),
    path('', views.post_list, name = 'post_list'),
    path('<int:pk>/',views.post_detail, name='post_detail'),#re_path(r'(?P<pk>\d+)/$', views.post_detail), #위와 같은의미

    # path('archives/<year:year>/', views.archives_year),
    #path('archives/<int:year>/', views.archives_year),
    #re_path(r'archives/(?P<year>\d+)/', views.archives_year), #정규포현식을 사용 원하는 정확한 인자로 주소설정가능 (?P<year>\d+)
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_day'),

]