"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from member import views as member_views
from post import views as post_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('post/', post_views.post_list, name='post_list'),
    path('post/create/', post_views.post_create, name='post_create'),
    path('post/detail/<int:post_pk>/', post_views.post_detail, name='post_detail'),
    path('post/<int:post_pk>/comment/create/', post_views.comment_create, name='comment_create'),

    path('member/signup/', member_views.signup, name='signup'),
]

# URL resolver는 settings.MEDIA_URL로 온 URL은
# view를 찾는 게 아니라 document_root에서 파일을 찾아 리턴해준다.
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)