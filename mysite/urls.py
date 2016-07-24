"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from shellbook import views as shellbook_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', shellbook_views.home, name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'^login/personal_info/', shellbook_views.userinfo,name = 'userinfo'),
	url(r'^register/', shellbook_views.userregister,name = 'register'),
	url(r'^login/', shellbook_views.userlogin,name = 'login'),
	url(r'^static/(?P<path>.*)$','django.views.static.server',{'document_root':settings.STATIC_ROOT},name='static'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
