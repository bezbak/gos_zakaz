# Generated by Django 4.2.4 on 2023-08-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0015_tourismmedia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='resume_ky',
        ),
        migrations.AlterField(
            model_name='team',
            name='resume_ru',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
