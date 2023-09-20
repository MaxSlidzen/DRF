from django.urls import path
from rest_framework.routers import DefaultRouter

from courses.apps import CoursesConfig
from courses.views import CourseAPIViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentAPIViewSet

app_name = CoursesConfig.name

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_detail'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lessons_delete'),
]

router_course = DefaultRouter()
router_course.register(r'courses', CourseAPIViewSet, basename='courses')

router_payment = DefaultRouter()
router_payment.register(r'payments', PaymentAPIViewSet, basename='payments')

urlpatterns += router_course.urls
urlpatterns += router_payment.urls
