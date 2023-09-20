from django.conf import settings
from django.db import models

from users.models import NULLABLE, User


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    image = models.ImageField(upload_to='courses/courses/', verbose_name='превью курса', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    image = models.ImageField(upload_to='courses/lessons/', verbose_name='превью урока', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    link = models.URLField(verbose_name='ссылка', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    METHOD_CASH = 'cash'
    METHOD_TRANSFER = 'transfer'
    METHODS = (
        (METHOD_CASH, 'Наличные'),
        (METHOD_TRANSFER, 'Перевод'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный курс',
                               related_name='method')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='оплаченный урок',
                               related_name='method')
    payment = models.IntegerField(verbose_name='сумма')
    method = models.CharField(max_length=20, choices=METHODS, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.user} - {self.payment}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
