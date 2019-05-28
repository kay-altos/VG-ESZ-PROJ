from django.db import models
from django.contrib import messages
from staicsitecontent.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
#
class ContractTemplates(models.Model):
    templ = models.TextField()

class Role(models.Model):
    RoleName = models.CharField(max_length=30)
    RoleLabel = models.CharField(max_length=30)
    RoleDescription = models.TextField()
#

class SuddopConstants(models.Model):
    SConstName = models.CharField(max_length=30)
    SConstValue = models.TextField()
    SConstDescription = models.TextField(default='')
    def __str__(self):
        return self.SConstName
#

class User(models.Model):
    Name = models.CharField(max_length=100)
    Login = models.CharField(max_length=20)
    Password = models.CharField(max_length=16)
    Roles = models.ManyToManyField(Role)
#
class ContractStatus(models.Model):
    Status = models.CharField(max_length=30)
    def __str__(self):
        return self.Status
#
class Applicant(models.Model):
    FirstName = models.CharField(max_length=30, verbose_name="Фамилия")
    LastName = models.CharField(max_length=30, verbose_name="Имя")
    Patronymic = models.CharField(max_length=30, verbose_name="Отчество")
    FullName = models.CharField(max_length=180, verbose_name="ФИО полностью")
    ApplicantSnils = models.CharField(max_length=11, null=True, blank=True, verbose_name="СНИЛС")
    #ApplicantEmail = models.CharField(max_length=150, verbose_name="Контактный Email")
    #ApplicantPhone = models.CharField(max_length=12, verbose_name="Контактный телефон")
    def __str__(self):
        ApplicantVar = Applicant.objects.get(id=self.id)
        #ApplicantPassportVar = ApplicantPassport.objects.get(Applicant=ApplicantVar)
        ApplicantPhonesVar = ApplicantPhones.objects.get(Applicant=ApplicantVar)
        return '%s, контактный телефон: %s' % (self.FullName, ApplicantPhonesVar.Phone)
    def save(self, *args, **kwargs):
        pass
        super(Applicant, self).save(*args, **kwargs)
    class Meta:
            verbose_name="Заявитель"
            verbose_name_plural="Заявители"
#
@receiver(post_save, sender=Applicant)
def update_ApplicantPasport(sender, instance, **kwargs):
    try:
        ApplicantPassport.objects.get(Applicant = Applicant.objects.get(id = instance.id))
    except ApplicantPassport.DoesNotExist:
        ap = ApplicantPassport()
        ap.Applicant =  instance
        ap.ApplicantDocWhomWhenIssued = "Не заполнено"
        ap.ApplicantAddress = "Не заполнено"
        ap.SerialPaspDoc = "0000"
        ap.NumPaspDoc = "000000"
        ap.DataOutDoc = "1900-01-01"
        ap.save()
#
class ApplicantEmails(models.Model):
    Applicant = models.OneToOneField(Applicant, on_delete = models.CASCADE, primary_key = True, unique=True, verbose_name="Заявитель")
    Email = models.CharField(max_length=30, unique=True, null=False, verbose_name="Адрес электронной почты")
    def __str__(self):
        return self.Applicant.FullName
    class Meta:
        verbose_name = "Адрес электронной почты"
        verbose_name_plural = "Адреса электронной почты"
#
class ApplicantPhones(models.Model):
    Applicant = models.OneToOneField(Applicant, on_delete = models.CASCADE, primary_key = True, unique=True, verbose_name="Заявитель")
    Phone = models.CharField(max_length=30, unique=True, null=False, verbose_name="Телефон")
    def __str__(self):
        return self.Applicant.FullName
    class Meta:
        verbose_name = "Телефон заявителя"
        verbose_name_plural = "Телефоны заявителей"
#
class ApplicantPassport(models.Model):
    Applicant = models.OneToOneField(Applicant, on_delete = models.CASCADE, primary_key = True, unique=True, verbose_name="Заявитель")
    ApplicantDocWhomWhenIssued = models.TextField(verbose_name="Кем и когда выдан", null=True, blank=True)
    ApplicantAddress = models.TextField(null=True, blank=True, verbose_name="Адрес регистрации")
    SerialPaspDoc = models.CharField(null=True, blank=True, max_length=4, verbose_name="Серия")
    NumPaspDoc = models.CharField(null=True, blank=True, max_length=6, verbose_name="Номер")
    DataOutDoc = models.DateField(null=True, blank=True, verbose_name="Дата выдачи")
    def __str__(self):
        return '%s - Паспорт - серия: %s / номер: %s' % (self.Applicant.FullName, self.SerialPaspDoc, self.NumPaspDoc)

    class Meta:
        verbose_name="Документ удостоверяющий личность"
        verbose_name_plural="Документы удостоверяющие личность"
#
GENDERCHOICE = (
    ('Мужской','Мужской'),
    ('Женский','Женский'),
    ('Не определен','Не определен'),

)
DOCTYPECHOICE = (
    ('Метрика', 'Метрика'),
    ('СНИЛС', 'СНИЛС'),
    ('Требует заполнения', 'Требует заполнения'),

)
class Student(models.Model):
    Name = models.CharField(max_length=30, verbose_name="ФИО (полностью)")
    DateBirth = models.DateField(verbose_name="Дата рождения")
    Group = models.ManyToManyField(Group, verbose_name="Учебная группа")
    Applicant = models.ForeignKey(Applicant, on_delete = models.CASCADE, verbose_name='Законный представитель')
    DocumentType = models.CharField(max_length=20, choices=DOCTYPECHOICE, verbose_name="Тип документа", null=True, default="Не определен")
    SeriaNumDoc = models.CharField(max_length=11,verbose_name="Номер", null=True)
    DatarRegDoc = models.DateField(verbose_name="Дата регистрации", null=True)
    GenderLabel = models.CharField(max_length=15, choices=GENDERCHOICE, verbose_name="Пол", default="-")

    def __str__(self):
        aph = ApplicantPhones.objects.get(Applicant = self.Applicant)
        return 'Обуч.: %s, pак.пред.: %s, %s' % (self.Name, self.Applicant.FullName, aph.Phone)
    class Meta:
        verbose_name="Обучающийся"
        verbose_name_plural="Обучающиеся"
#

class Contract(models.Model):
    Date = models.DateField(verbose_name='Дата договора')
    Number = models.CharField(max_length=30, verbose_name='Номер договора')
    Applicant = models.ForeignKey(Applicant, on_delete = models.CASCADE, verbose_name='Заявитель')
    Student = models.ForeignKey(Student, on_delete = models.CASCADE, verbose_name='Обучающийся')
    Program = models.ForeignKey(Program, on_delete = models.CASCADE, verbose_name='Программа')
    EducationForm = models.ForeignKey(EducationForm, on_delete = models.CASCADE, verbose_name='Форма обучения')
    LessonBeginDate = models.DateField(verbose_name='Дата начала занятий')
    LessonEndDate = models.DateField(verbose_name='Дата окончания занятий')
    MasteringProgramBeginDate = models.DateField(verbose_name='Дата начала под. занятий')
    MasteringProgramEndDate = models.DateField(verbose_name='Дата окончания под. занятий')
    EducationYear = models.ForeignKey(EducationYear, on_delete = models.CASCADE, verbose_name='Год обучения')
    ContractStatus = models.ForeignKey(ContractStatus, null=True, on_delete=models.SET_NULL, verbose_name='Статус договора')
    ContractType = models.ForeignKey(ContractType, null=True, on_delete=models.SET_NULL, verbose_name='Тип договора')
    #AppFiledOnMosRu = models.BooleanField()
    def __str__(self):
        return self.Number
    class Meta:
        permissions = (("can_can", "Can Do"),)
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
    def save(self, *args, **kwargs):
        if self.ContractStatus is None:
            '''1 - Не подписан, 2 - Подписан по СМС'''
            self.ContractStatus = ContractStatus.objects.get(id=1)
        super(Contract, self).save(*args, **kwargs)

@receiver(post_save, sender=Contract)
def update_ContractSignTransaction(sender, instance, **kwargs):
    try:
        ContractSignTransaction.objects.get(Contract = Contract.objects.get(id = instance.id))
    except ContractSignTransaction.DoesNotExist:
        csitr = ContractSignTransaction(
            Contract = Contract.objects.get(id = instance.id),
            ContractSignTransactionState = ContractSignTransactionState.objects.get(id=97)
            )
        csitr.save()
#

class ContractSign(models.Model):
    SignKey =  models.CharField(max_length=32, null=False,  unique=True,)
    Contract = models.OneToOneField(Contract, on_delete = models.CASCADE, primary_key = True, unique=True, verbose_name="Договор")
    SmsCode =  models.CharField(max_length=32, null=True,  unique=True,)

class SendSmsTransactionState(models.Model):
    '''
    State = 1, SatateLabel = Задание поставлено в очередь на обработку
    State = 2, SatateLabel = Сообщение отправлено
    State = 3, SatateLabel = Сообщение доставлено
    State = 4-99 -  reserve
    State = 99, SatateLabel = Возникла ошибка. Подробности в логе.
    '''
    SatateLabel = models.CharField(max_length=100)
#
class SendEmailTransactionState(models.Model):
    '''
    State = 1, SatateLabel = Задание поставлено в очередь на обработку
    State = 2, SatateLabel = Сообщение отправлено
    State = 3, SatateLabel = Сообщение доставлено
    State = 4-99 -  reserve
    State = 99, SatateLabel = Возникла ошибка. Подробности в логе.
    '''
    SatateLabel = models.CharField(max_length=100)
    def __str__(self):
        return self.SatateLabel
#
class ContractSignTransactionState(models.Model):
    '''
    State = 1, SatateLabel = Заявитель перешел по индивидуальной ссылке
    State = 2, SatateLabel = Смс с кодом отправлено
    State = 3, SatateLabel = Договор подписан
    State = 4-99 -  reserve
    State = 97, SatateLabel = Новый договор.
    State = 98, SatateLabel = Письмо направлено заявителю.
    State = 99, SatateLabel = Возникла ошибка. Подробности в логе.
    '''
    SatateLabel = models.CharField(max_length=100)
    def __str__(self):
        return self.SatateLabel
#
class ContractSignTransaction(models.Model):
    Contract = models.ForeignKey(Contract, on_delete = models.CASCADE, verbose_name='')
    ContractSignTransactionState = models.ForeignKey(ContractSignTransactionState, on_delete = models.CASCADE, verbose_name='')
    def __str__(self):
        return self.ContractSignTransactionState.SatateLabel


class EmailTransaction(models.Model):
    Contract = models.ForeignKey(Contract, on_delete = models.CASCADE, verbose_name='')
    SendEmailTransactionState = models.ForeignKey(SendEmailTransactionState, on_delete = models.CASCADE, verbose_name='')
