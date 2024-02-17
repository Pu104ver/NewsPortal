from django.urls import path
from django.views.decorators.cache import cache_page

from .views import NewsList, NewsDetail, PostSearchView, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, \
    ArticleUpdate, ArticleDelete

urlpatterns = [
    # path('', cache_page(1 * 60)(NewsList.as_view()), name='post_list'),
    path('', NewsList.as_view(), name='post_list'),
    path('<int:pk>', cache_page(5 * 60)(NewsDetail.as_view()), name='post_detail'),
    path('search/', cache_page(5 * 60)(PostSearchView.as_view()), name='post_search'),
    path('news/create/', cache_page(5 * 60)(NewsCreate.as_view()), name='news_create'),
    path('news/<int:pk>/update/', cache_page(5 * 60)(NewsUpdate.as_view()), name='news_update'),
    path('news/<int:pk>/delete/', cache_page(5 * 60)(NewsDelete.as_view()), name='news_delete'),
    path('article/create/', cache_page(5 * 60)(ArticleCreate.as_view()), name='article_create'),
    path('article/<int:pk>/update/', cache_page(5 * 60)(ArticleUpdate.as_view()), name='article_update'),
    path('article/<int:pk>/delete/', cache_page(5 * 60)(ArticleDelete.as_view()), name='article_delete'),

]
