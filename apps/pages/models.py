from django.db import models

# Create your models here.
class Police(models.Model):
    text = models.TextField()
    text_ru = models.TextField()
    def __str__(self):
        return f"Политика конфеденцеальности: {self.id}"
    class Meta:
        verbose_name = 'Политика конфеденцальности'
        verbose_name_plural = 'Политика конфеденцальности'
    
class StateSymbols(models.Model):
    text = models.TextField()
    text_ru = models.TextField()
    def __str__(self):
        return f"Гос. символ: {self.id}"
    class Meta:
        verbose_name = 'Гос. символ'
        verbose_name_plural = 'Гос. символы'

class DevFund(models.Model):
    text = models.TextField()
    text_ru = models.TextField()
    def __str__(self):
        return f":Фонд развития {self.id}"
    class Meta:
        verbose_name = 'Фонд развития'
        verbose_name_plural = 'Фонды развития'

class Rayons(models.Model):
    name = models.CharField(
        verbose_name='Название района',
        max_length=50
    )
    text = models.TextField()
    text_ru = models.TextField()
    def __str__(self):
        return f":Район {self.name}"
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'