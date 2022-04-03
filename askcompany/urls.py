"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from django.conf import global_settings
#from askcompany.urls import settings     이렇게 사용하면 안된다
from django.conf import settings # 위에 두개를 한번에 사용가능

from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    #path('',TemplateView.as_view(template_name='root.html'), name='root'),
    path('',RedirectView.as_view(
        #url = "/instagram/"
        pattern_name = "instagram:post_list", #url_reverse app_name과 path 인자 name 지정되있을떄 사용가능
        ), name='root'),

    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')),
    path('pratice/', include('practice.urls')),
    path('instagram/', include('instagram.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG: #DEBUG가 참일떄만 개발모드일때만 True임
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    #하는 이유 settings.py에 MEDIA_URL 설정해 두었지만 urls에서 페이지설정 따로하지않아 urlpatterns에 추가해야 해당 파일 url 사용가능

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

#askcompany setting을 가지고왔다.
#settings.MEDIA_URL
#settings.MEDIA_ROOT