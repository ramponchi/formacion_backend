from django.urls import include, path, re_path
from management.views import UsersList

urlpatterns = [
    path('users', UsersList.as_view(), name='Users'),
]