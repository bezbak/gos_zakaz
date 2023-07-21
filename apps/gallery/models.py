from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(
        'Фото для галлереи',
        upload_to='gallery/'
    )
    
    def __str__(self):
        return f'Фото номер {self.id}'
    
    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        
class Video(models.Model):
    video=models.FileField(
        'Видео для галлереи',
        upload_to='gallery/'
    )
    
    def __str__(self):
        return f'Видео номер {self.id}'
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'