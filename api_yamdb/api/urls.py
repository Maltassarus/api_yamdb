from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import SignUpViewSet

app_name = 'api'

router = SimpleRouter()
router.register('auth/signup', SignUpViewSet)


urlpatterns = [
    #path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
