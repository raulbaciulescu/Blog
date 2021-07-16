from django.conf import settings
from django.template.context_processors import static
from django.urls import path, include

from posts.views import PostList, index, PostDetail, search

app_name = 'posts'
urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('index/', index, name='index'),
    path('search/', search, name='search'),
    path('posts/<pk>/', PostDetail.as_view(), name='detail'),
]