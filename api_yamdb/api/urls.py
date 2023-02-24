from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, GenreViewSet, SignUpViewSet, TitleViewSet,
                    UserViewSet, token)

app_name = 'api'

router = SimpleRouter()
router.register('auth/signup', SignUpViewSet)
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet,
                basename='categories')
router.register('genres', GenreViewSet,
                basename='genres')
router.register('titles', TitleViewSet,
                basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', token, name='token')
]
