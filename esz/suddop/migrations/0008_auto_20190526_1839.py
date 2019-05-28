# Generated by Django 2.2 on 2019-05-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suddop', '0007_auto_20190526_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DocumentType',
            field=models.CharField(choices=[('M', 'Метрика'), ('S', 'СНИЛС'), ('-', 'Не определен')], default='Не определен', max_length=1, null=True, verbose_name='Тип документа'),
        ),
        migrations.AlterField(
            model_name='student',
            name='GenderLabel',
            field=models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский'), ('Не определен', 'Не определен')], default='-', max_length=15, verbose_name='Пол'),
        ),
    ]
