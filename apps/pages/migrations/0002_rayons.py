# Generated by Django 4.2.4 on 2023-08-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rayons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название района')),
                ('name_ky', models.CharField(max_length=50, null=True, verbose_name='Название района')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Название района')),
                ('text', models.TextField()),
                ('text_ru', models.TextField()),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
    ]
