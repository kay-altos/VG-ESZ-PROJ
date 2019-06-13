# Generated by Django 2.2 on 2019-05-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suddop', '0003_auto_20190525_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantpassport',
            name='ApplicantAddress',
            field=models.TextField(blank=True, null=True, verbose_name='Адрес регистрации'),
        ),
        migrations.AlterField(
            model_name='applicantpassport',
            name='ApplicantDocWhomWhenIssued',
            field=models.TextField(blank=True, null=True, verbose_name='Кем и когда выдан'),
        ),
        migrations.AlterField(
            model_name='applicantpassport',
            name='DataOutDoc',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выдачи'),
        ),
        migrations.AlterField(
            model_name='applicantpassport',
            name='NumPaspDoc',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='applicantpassport',
            name='SerialPaspDoc',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Серия'),
        ),
    ]