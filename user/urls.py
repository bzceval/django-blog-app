from django.urls import path, include  
from .views import UserView
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', UserView)

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('login', obtain_auth_token),
]