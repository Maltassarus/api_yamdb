from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (SignUpViewSet, token,
                    CategoryCreateListDestroyViewSet,
                    GenreCreateListDestroyViewSet)

app_name = 'api'

router = SimpleRouter()
router.register('auth/signup', SignUpViewSet)
router.register('categories', CategoryCreateListDestroyViewSet,
                basename='categories')
router.register('genres', GenreCreateListDestroyViewSet,
                basename='genres')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', token, name='token')
]
