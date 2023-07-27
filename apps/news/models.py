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
        
class Media(models.Model):
    image = models.ImageField(
        'Доп фото для новости',
        upload_to='news_images/'
    )
    news = models.ForeignKey(
        News,
        related_name='media',
        on_delete=models.CASCADE,
        verbose_name='Новость'
    )
    def __str__(self):
        return f"Фото:{self.news.title} номер {self.id}"
   
    class Meta:
        verbose_name = 'Доп фото новости'
        verbose_name_plural = 'Доп фото новости'