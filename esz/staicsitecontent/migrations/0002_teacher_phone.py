# Generated by Django 2.2 on 2019-05-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staicsitecontent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Phone',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='Телефон'),
        ),
    ]
