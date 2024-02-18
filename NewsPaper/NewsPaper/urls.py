
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news.views import subscriptions, my_view, Index, PostViewSet, NewsViewSet, ArticlesViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'articles', ArticlesViewSet, basename='articles')

urlpatterns = [
   path('i18n/', include('django.conf.urls.i18n')),
   path('admin/', admin.site.urls),
   path('posts/', include('news.urls')),
   path("accounts/", include("allauth.urls")),
   path('subscriptions/', subscriptions, name='subscriptions'),
   path('test-error/', my_view, name='test-error'),
   path('', Index.as_view()),
   path('api/', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]