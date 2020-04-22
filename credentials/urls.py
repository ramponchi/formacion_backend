from django.urls import include, path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Submit your refresh token to this path to obtain a new access token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]