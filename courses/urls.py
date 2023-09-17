from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.apps import CoursesConfig
from courses.views import CourseAPIViewSet

app_name = CoursesConfig.name

urlpatterns = [

]

router = DefaultRouter()
router.register(r'courses', CourseAPIViewSet, basename='courses')

urlpatterns += router.urls
