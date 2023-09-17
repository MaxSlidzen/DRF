from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    image = models.ImageField(upload_to='users/', verbose_name='превью курса', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
