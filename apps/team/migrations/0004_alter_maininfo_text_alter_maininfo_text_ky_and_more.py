# Generated by Django 4.2.4 on 2023-08-08 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_maininfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfo',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='text_ky',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='maininfo',
            name='text_ru',
            field=models.TextField(null=True),
        ),
    ]
