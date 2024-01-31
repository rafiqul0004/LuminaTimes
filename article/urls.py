from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('article_list', views.ArticleViewSet)
router.register('category', views.CategoryViewSet)
router.register('review', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.ArticleCreateView.as_view({'post': 'create'}), name='article_create'),
    path('review_create/<int:pk>/', views.ReviewCreateViewSet.as_view({'post': 'create'}), name='review_create'),
    path('article_list/<int:pk>/', views.UpdateArticleView.as_view(), name='article_update'),
]