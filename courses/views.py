from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from courses.models import Course, Lesson, Payment
from courses.permissions import AuthorOrModerator, AuthorOrModeratorOrCustomer, OnlyAuthor, NotModerator
from courses.serializers import CourseSerializer, LessonSerializer, PaymentSerializer


class CourseAPIViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permissions = {
        'create': NotModerator,
        'retrieve': AuthorOrModeratorOrCustomer,
        'update': AuthorOrModerator,
        'partial_update': AuthorOrModerator,
        'destroy': OnlyAuthor
    }

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, self.permissions.get(self.action)]
        return super().get_permissions()

    def perform_create(self, serializer):
        self.permission_classes = [NotModerator]
        new_course = serializer.save()
        new_course.author = self.request.user
        new_course.save()


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [NotModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AuthorOrModeratorOrCustomer]


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AuthorOrModerator]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [OnlyAuthor]


class PaymentAPIViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method')
    ordering_fields = ('payment_date',)
