# Generated by Django 2.2 on 2019-05-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staicsitecontent', '0002_teacher_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Phone',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True, verbose_name='Телефон'),
        ),
    ]
