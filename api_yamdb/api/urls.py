from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import SignUpViewSet, token

app_name = 'api'

router = SimpleRouter()
router.register('auth/signup', SignUpViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', token, name='token')
]
