# Generated by Django 4.2.3 on 2023-07-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Struct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название структуры')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Структура',
                'verbose_name_plural': 'Структуры',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55, verbose_name='ФИО')),
                ('job_title', models.CharField(max_length=50, verbose_name='Должность')),
                ('image', models.ImageField(upload_to='team/', verbose_name='Фото работника')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Руководство',
            },
        ),
    ]
