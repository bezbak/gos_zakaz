from django.db import models

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(
        'ФИО',
        max_length=55
    )
    job_title = models.CharField(
        'Должность',
        max_length=50
    )
    image = models.ImageField(
        'Фото работника',
        upload_to='team/'
    )
    resume = models.TextField()
    resume_ru = models.TextField()
    phone = models.CharField(
        'Номер телефона',
        max_length=20
    )
    
    def __str__(self):
        return f"{self.full_name} : {self.job_title}"
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Руководство'
        
class Struct(models.Model):
    name = models.CharField(
        'Название структуры',
        max_length=50
    )
    description = models.TextField()
    phone = models.CharField(
        'Номер телефона',
        max_length=20
    )
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Структура'
        verbose_name_plural = 'Структуры'
        
class MainInfo(models.Model):
    text = models.TextField()
    text_ru = models.TextField()
    def __str__(self):
        return f"Инфо: {self.id}"
    class Meta:
        verbose_name = 'Главная информация'
        verbose_name_plural = 'Главная информация'

class Tourism(models.Model):
    text = models.TextField()
    text_ru = models.TextField()
    def __str__(self):
        return f"Туризм: {self.id}"
    class Meta:
        verbose_name = 'Для Туристов'
        verbose_name_plural = 'Для Туристов'

class TourismMedia(models.Model):
    image = models.ImageField(
        'Фото для Туризма',
        upload_to='tourism_media/'
    )
    tour = models.ForeignKey(
        Tourism,
        related_name='media',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"Фото туризма: {self.id}"

    class Meta:
        verbose_name = 'Фото для туризма'
        verbose_name_plural = 'Фото для туризма'

class Corruption(models.Model):
    text = models.TextField()
    text_ru = models.TextField()
    def __str__(self):
        return f"Коррупция: {self.id}"
    class Meta:
        verbose_name = 'Информациия о противодействии коррупции'
        verbose_name_plural = 'Информациия о противодействии коррупции'

class Links(models.Model):
    email = models.EmailField()
    phone1 = models.CharField(max_length=25)
    phone2 = models.CharField(max_length=25)
    fax = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
class GosLinks(models.Model):
    name = models.CharField(
        max_length=50
    )
    url = models.URLField(
        max_length=200
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Ссылка на гос сайт'
        verbose_name_plural = 'Ссылки на гос сайты'

class Images(models.Model):
    main_image = models.ImageField(
        upload_to='images/'
    )

