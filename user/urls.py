from django.urls import path, include  
from .views import UserView
from rest_framework.authtoken.views import obtain_auth_token

# ----------------------------------------------------------------
# Logout function:
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET', 'POST'])
def logout(request):
    request.user.auth_token.delete() # Token Sil.
    return Response({"message": 'User Logout: Token Deleted'})
# ----------------------------------------------------------------

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', UserView)

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('login', obtain_auth_token),
    path('logout', logout),
]