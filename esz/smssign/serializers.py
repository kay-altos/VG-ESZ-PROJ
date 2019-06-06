from rest_framework import serializers
from suddop.models import *
#serializers.Serializer
#
class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
#
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'
#
class ApplicantEmailsSerializer(serializers.ModelSerializer):
    #applicant = ApplicantSerializer(source='Applicant', many=False)
    class Meta:
        model = ApplicantEmails
        fields = '__all__'
#
class ApplicantPhonesSerializer(serializers.ModelSerializer):
    #applicant = ApplicantSerializer(source='Applicant', many=False)
    class Meta:
        model = ApplicantPhones
        fields = '__all__'
#
class ApplicantPassportSerializer(serializers.ModelSerializer):
    #applicant = ApplicantSerializer(source='Applicant', many=False)
    class Meta:
        model = ApplicantPassport
        fields = '__all__'
#
class PageGreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuddopConstants
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    applicant = ApplicantSerializer(source='Applicant', many=False)
    program = ProgramSerializer(source='Program', many=False)
    class Meta:
        model = Contract
        fields = '__all__'


    '''
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

class Applicant(models.Model):
    FirstName = models.CharField(max_length=30, verbose_name="Фамилия")
    LastName = models.CharField(max_length=30, verbose_name="Имя")
    Patronymic = models.CharField(max_length=30, verbose_name="Отчество")
    FullName = models.CharField(max_length=180, verbose_name="ФИО полностью")
    ApplicantSnils = models.CharField(max_length=11, null=True, blank=True, verbose_name="СНИЛС")
    #ApplicantEmail = models.CharField(max_length=150, verbose_name="Контактный Email")
    #ApplicantPhone = models.CharField(max_length=12, verbose_name="Контактный телефон")
    Date = serializers.DateField()
    Number = serializers.CharField()
    Applicant = serializers.CharField()
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
    '''
