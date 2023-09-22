from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course, Lesson, Payment


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(read_only=True, many=True, source='lesson')

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lessons(self, instance):
        return instance.lesson.all().count()


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
