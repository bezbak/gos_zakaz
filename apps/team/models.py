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
    phone = models.CharField(
        'Номер телефона',
        max_length=20
    )
    email = models.CharField(
        'Почта',
        max_length=50
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
    def __str__(self):
        return f"Инфо: {self.id}"
    class Meta:
        verbose_name = 'Главная информация'
        verbose_name_plural = 'Главная информация'

class Tourism(models.Model):
    text = models.TextField()
    def __str__(self):
        return f"Туризм: {self.id}"
    class Meta:
        verbose_name = 'Для Туристов'
        verbose_name_plural = 'Для Туристов'