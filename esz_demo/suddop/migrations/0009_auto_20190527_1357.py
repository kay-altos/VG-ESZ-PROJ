# Generated by Django 2.2 on 2019-05-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suddop', '0008_auto_20190526_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DocumentType',
            field=models.CharField(choices=[('Метрика', 'Метрика'), ('СНИЛС', 'СНИЛС'), ('Требует заполнения', 'Требует заполнения')], default='Не определен', max_length=20, null=True, verbose_name='Тип документа'),
        ),
    ]