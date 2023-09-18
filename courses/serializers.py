from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lessons = SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


    def get_lessons(self, instance):
        return instance.lesson_set.all().count()


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
