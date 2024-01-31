from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register('viewerlist', views.ViewerViewSet)
router.register('editorlist', views.EditorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(),name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>',views.activate,name='activate'),
]