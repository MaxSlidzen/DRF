from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserAPIViewSet

app_name = UsersConfig.name

urlpatterns = [

]

router = DefaultRouter()
router.register(r'', UserAPIViewSet, basename='users')

urlpatterns += router.urls
