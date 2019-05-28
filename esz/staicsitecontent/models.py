from django.db import models
from django.utils.safestring import mark_safe
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.conf import settings
#from staicsitecontent.models import *
# Create your models here.
#
class Category(models.Model):
    Cat_Name = models.CharField(max_length=200, verbose_name='Название категории')
    Cat_Description = models.TextField(max_length=4096, verbose_name='Опиание категории')
    Cat_photo = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=100, verbose_name='Загрузка изображения')
    def __str__(self):
        return self.Cat_Name
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def headshot_image(self):
        return mark_safe('<img  class="img-thumbnail" src="http://dev.esz.dvorec.net/media/{url}" width="250px" height="250px" />'.format(
            url = self.Cat_photo,

            )
    )
    headshot_image.short_description = 'Предпросмотр'
    headshot_image.allow_tags = True

class Center(models.Model):
    Name = models.CharField(max_length=250, verbose_name="Название центра")
    ShortName = models.CharField(max_length=100, verbose_name="Краткое название центра")
    Description = models.TextField(max_length=2048,verbose_name="Описание")
    Code = models.CharField(max_length=30,verbose_name="Код")
    Address = models.TextField(max_length=100,verbose_name="Адрес")
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name="Центр"
        verbose_name_plural="Центры"

#
class FinancingType(models.Model):
    Type = models.CharField(max_length=30, verbose_name="Тип финансирования")
    def __str__(self):
        return self.Type
    class Meta:
        verbose_name="Тип финансирования"
        verbose_name_plural="Типы финансирования"

#
class Program(models.Model):
    Name = models.CharField(max_length=30, verbose_name="Наименование программы")
    ShortName = models.CharField(max_length=30, verbose_name="Краткое название")
    Description = models.TextField(verbose_name="Описание программы")
    IdImage = models.IntegerField(null=True)
    Code = models.CharField(max_length=30, verbose_name="Код программы")
    Center = models.ForeignKey(Center, null=True, on_delete=models.SET_NULL, verbose_name="Центр")
    FinancingType = models.ForeignKey(FinancingType, null=True, on_delete=models.SET_NULL, verbose_name="Тип финансирования")
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name="Программа обучения"
        verbose_name_plural="Программы обучения"
#
@deconstructible
class UploadToPathAndRename(object):
    def __init__(self, path):
        self.sub_path = path
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)
#

class Teacher(models.Model):
    FullName = models.CharField(max_length=100, verbose_name="ФИО")
    Phone =  models.CharField(max_length=16, unique=True, null=True, blank=True, verbose_name="Телефон")
    ProgramLeadsTeacher = models.ManyToManyField(Program, verbose_name="Предмет")
    #Photo = models.ImageField(upload_to='img/teachers', null=True, blank=True, height_field=None, width_field=None, max_length=100, verbose_name='Загрузка изображения')
    Photo = models.FileField(upload_to=UploadToPathAndRename(os.path.join('esz/media', 'img', 'teachers')), null=True, blank=True, max_length=100, verbose_name='Загрузка изображения')

    def __str__(self):
        return self.FullName
    class Meta:
        verbose_name="Педагог"
        verbose_name_plural="Педагоги"
    def headshot_image(self):
        if self.Photo != '':
            return mark_safe('<img  class="img-thumbnail" src="http://dev.esz.dvorec.net/media/{url}" width="250px" height="250px" />'.format(
                url = self.Photo,
                )
            )
        else:
            return mark_safe('<img  class="img-thumbnail" src="http://dev.esz.dvorec.net/media/{url}" width="250px" height="250px" />'.format(
                url = 'default/default_photo.png',
                )
            )
    headshot_image.short_description = 'Предпросмотр'
    headshot_image.allow_tags = True
#
class Group(models.Model):
    Name = models.CharField(max_length=30, verbose_name="Название группы")
    ShortName = models.CharField(max_length=30, verbose_name="Короткое название группы")
    Code = models.CharField(max_length=30, verbose_name="Код группы")
    Program = models.ForeignKey(Program, null=True, on_delete=models.SET_NULL, verbose_name="Программа обучения")
    Teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL, verbose_name="Педагог")
    Center = models.ForeignKey(Center, null=True, on_delete=models.SET_NULL, verbose_name="Центр")
    #Student = models.ForeignKey(Student, on_delete = models.CASCADE, verbose_name="Обучающийся")
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name="Группа обучения"
        verbose_name_plural="Группы обучения"


class ContractType(models.Model):
    Type = models.CharField(max_length=30)
    def __str__(self):
        return self.Type
    class Meta:
        verbose_name="Тип договора"
        verbose_name_plural="Типы договора"

#
class EducationForm(models.Model):
    EducationForm = models.CharField(max_length=100, verbose_name="Форма обучения")
    def __str__(self):
        return self.EducationForm
    class Meta:
        verbose_name="Форма обучения"
        verbose_name_plural="Формы обучения"

#
class EducationYear(models.Model):
    EducationYear = models.CharField(max_length=10, unique=True, verbose_name="Год обучения")
    def __str__(self):
        return self.EducationYear
    class Meta:
        verbose_name="Год обучения"
        verbose_name_plural="Годы обучения"
