from django.db import models

# Create your models here.

class News(models.Model):
    image = models.ImageField(
        'Фото новости',
        upload_to='news_images/'
    )
    title = models.CharField(
        'Загаловок новости',
        max_length=55
    )
    description = models.TextField(
        'Описание новости'
    )
    created = models.DateField(
        auto_now_add=True
    )
    
    def __str__(self):
        return f'Новость: {self.title} || Дата {self.created}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'