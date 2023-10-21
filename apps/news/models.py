from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class News(models.Model):
    image = models.ImageField(
        _('Жаңылыктын сүрөтү'),
        upload_to='news_images/'
    )
    title = models.CharField(
        _('Жаңылыктын башы'),
        max_length=55
    )
    description = models.TextField(
        _('Жаңылыктын сүрөттөлүшү')
    )
    description_ru = models.TextField(
        _('Жаңылыктын сүрөттөлүшү')
    )
    created = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'Новость: {self.title} || Дата {self.created}'
    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'id':self.id})

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
        verbose_name = 'Доп Жаңылыктын сүрөтү'
        verbose_name_plural = 'Доп Жаңылыктын сүрөтү'