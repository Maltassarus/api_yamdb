from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import SignUpViewSet, UserViewSet, token

app_name = 'api'

router = SimpleRouter()
router.register('auth/signup', SignUpViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', token, name='token')
]
