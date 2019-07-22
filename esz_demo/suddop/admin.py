from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *
from .forms import *
from django.utils.html import format_html
from django.urls import reverse
from smssign import urls,views
from django.urls import include, re_path
from django.template.response import TemplateResponse
import random
import string
from django.shortcuts import redirect
from .tasks import send_sms_sign, send_mail_sign
import logging
from django.contrib import messages
import smtplib
from django.http import HttpResponseRedirect
#
def randomStringDigits(stringLength=32):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
#


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """docstring fs CategiryAdmin."""
    form = CategoryForm
    fields = (
        'Cat_Name',
        'Cat_Description',
        'Cat_photo',
        'headshot_image',

    )
    readonly_fields = ('headshot_image',)



@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        ''''''
        var = 1
        if var:
            return super().delete_model(request, obj)
        """Если какая-то проверка успешна - удалить объект, если нет, то показать сообщение об ошибке."""
        messages.set_level(request, messages.ERROR)
        message = "НЕльзя удалить заблокированный договор"
        # Посылаем свое сообщение об ошибке.
        self.message_user(request, message, level=messages.ERROR)
    delete_model.short_description = "Удалить объекты"
    form = ContractForm
    #fields = ('Number','Date')
    fields = (
        'Number',
        'Date',
        'ContractType',
        'EducationYear',
        'Applicant',
        'Student',
        'Program',
        'EducationForm',
        'LessonBeginDate',
        'LessonEndDate',
        'MasteringProgramBeginDate',
        'MasteringProgramEndDate',
    )
#
    list_display = (
        'Number',
        'Applicant',
        'Contract_signStatus',
        'tranzaction_status',
        'Contract_actions'
    )
    #search_fields = ('Number','Applicant',)

#
    actions = [delete_model]
#
    def process_sign(self, request, contract_id, *args, **kwargs):
        data = {
            'form':  ContractSignForm,
            'opts': ContractSign._meta,
            'change': True,
            'is_popup': False,
            'save_as': False,
            'has_delete_permission': False,
            'has_add_permission': False,
            'has_change_permission': False
        }
#
        Contr = Contract.objects.get(id=contract_id)
        cstrs = ContractSignTransaction.objects.get(Contract = Contract.objects.get(id = contract_id))
        ApplicantPhone = ApplicantPhones.objects.get(Applicant=Contr.Applicant)
        ApplicantEmail = ApplicantEmails.objects.get(Applicant=Contr.Applicant)
        rnd_sign_contract = randomStringDigits(12)
        url_sign_contract = 'http://demo.contract.dvorec.net/contractsign/' + rnd_sign_contract
        contract_sign_message = 'Для подписания договора ВГ - %s, перейдите по ссылке %s' % (Contr.Number, url_sign_contract,)
#
        if request.method == 'GET':
            data['contract_id'] = contract_id
            data['cNumber'] = Contr.Number
            data['cApplicant'] = Contr.Applicant
            data['cDate'] = Contr.Date
            data['сStatus'] = Contr.ContractStatus
            data['cApplicantPhone'] = ApplicantPhone.Phone
            data['сEmail'] = ApplicantEmail.Email
            data['cstrs'] = cstrs
        if request.method == 'POST':
            Contr = Contract.objects.get(id=contract_id)
            ContrSign = ContractSign()
            ContrSign.Contract = Contr
            csc = randomStringDigits(32)
            ContrSign.SignKey = csc
            ContrSign.save()
            data['contract_id'] = contract_id
            data['cNumber'] = Contr.Number
            data['cApplicant'] = Contr.Applicant
            data['cDate'] = Contr.Date
            data['сStatus'] = Contr.ContractStatus
            data['cApplicantPhone'] = ApplicantPhone.Phone
            data['сEmail'] = ApplicantEmail.Email
            data['cstrs'] = cstrs
            #send_sms_sign.delay(contract_id, str(ApplicantPhone.Phone), contract_sign_message)
            send_mail_sign.delay(ApplicantEmail.Email, Contr.Number, contract_id, Contr.Applicant.FullName, csc)
            #return HttpResponseRedirect('')
#
        return TemplateResponse(request,'smssign/index.html', context=data)
#
    def get_urls(self):
        urls = super(ContractAdmin, self).get_urls()
        custom_urls = [
            re_path(r'^signsms/(?P<contract_id>.+)$', self.admin_site.admin_view(self.process_sign), name='process-sign'),
        ]
        return custom_urls + urls
#
    def tranzaction_status(self, obj):
        cstr = ContractSignTransaction.objects.get(Contract = obj)
        return format_html('<b>'+ cstr.ContractSignTransactionState.SatateLabel +'</b>')
    tranzaction_status.short_description = "Статус транзакции"
    def Contract_signStatus(self, obj):
        return format_html('<b>'+obj.ContractStatus.Status+'</b>')
    Contract_signStatus.short_description = "Стутас подписи по СМС"
    def Contract_actions(self, obj):
        return format_html('<a href="{}"><input type="button" value="Подробно..." /></a>',reverse('admin:process-sign',args=[obj.pk]))
    Contract_actions.short_description = "Действия с договором"
#
#
@admin.register(EducationYear)
class EducationYearAdmin(admin.ModelAdmin):
    form = EducationYearForm
    #fields = ('Number','Date')
    fields = (
        'EducationYear',
    )
#
@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    form = ContractTypeForm
    #fields = ('Number','Date')
    fields = (
        'Type',
    )
#
class ApplicantPassportInline(admin.StackedInline):
    model = ApplicantPassport
#
class ApplicantPhonesInline(admin.StackedInline):
    model = ApplicantPhones
#
class ApplicantEmailsInline(admin.StackedInline):
    model = ApplicantEmails
#
'''
class GenderInline(admin.StackedInline):
    model = Gender
#
class StudentDocsInline(admin.StackedInline):
    model = StudentDocs
#
'''
class GroupInline(admin.StackedInline):
    model = Group
#

class StudentInline(admin.StackedInline):
    model = Student
    extra = 0
    max_num = 4

#

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    form = ApplicantForm
    #fields = ('Number','Date')
    fields = (
        'FullName',
        'FirstName',
        'LastName',
        'Patronymic',
        'ApplicantSnils',
    )
    inlines = [  ApplicantPassportInline, ApplicantPhonesInline, ApplicantEmailsInline, StudentInline ]
    list_filter = ('FullName','ApplicantSnils',)
    list_display = ('FullName','Applicant_phone','Applicant_email','ApplicantSnils', 'Applicant_pasport',)
    #list_display_links = ('FullName','ApplicantSnils',)
    def Applicant_phone(self, obj):
        try:
            aph = ApplicantPhones.objects.get(Applicant = obj)
            return format_html('<b>'+ aph.Phone +'</b>')
        except ApplicantPhones.DoesNotExist:
            pass
    Applicant_phone.short_description = 'Телефон'
    def Applicant_email(self, obj):
        try:
            aem = ApplicantEmails.objects.get(Applicant = obj)
            return format_html('<b>'+ aem.Email +'</b>')
        except ApplicantEmails.DoesNotExist:
            pass
    Applicant_email.short_description = 'Электронная почта'

    def Applicant_pasport(self, obj):
        try:
            ApplicantVar = Applicant.objects.get(id=obj.id)
            ApplicantPassportVar = ApplicantPassport.objects.get(Applicant=ApplicantVar)
            return 'Серия: %s, Номер %s' % (ApplicantPassportVar.SerialPaspDoc, ApplicantPassportVar.NumPaspDoc)
        except ApplicantPassport.DoesNotExist:
            pass
    Applicant_pasport.short_description = 'Паспорт'

#

'''
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    form = GenderForm
    #fields = ('Number','Date')
    fields = (
        'GenderLabel',
    )
#
'''
@admin.register(FinancingType)
class FinancingTypeAdmin(admin.ModelAdmin):
    form = FinancingTypeForm
    #fields = ('Number','Date')
    fields = (
        'Type',
    )

@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    form = CenterForm
    #fields = ('Number','Date')
    fields = (
        'Name',
        'ShortName',
        'Description',
        'Code',
        'Address',
    )
#
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    form = ProgramForm
    #fields = ('Number','Date')
    fields = (
        'Name',
        'ShortName',
        'Description',
        'Code',
        'Center',
		'FinancingType'
    )
#
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    #fields = ('Number','Date')
    fields = (
        'FullName',
        'Phone',
        'ProgramLeadsTeacher',
        'Photo',
        'headshot_image'

    )
    readonly_fields = ('headshot_image',)
#
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    form = GroupForm
    #fields = ('Number','Date')
    fields = (
        'Name',
        'ShortName',
        'Code',
        'Program',
        'Teacher',
        'Center',
    )
#
'''
@admin.register(StudentDocs)
class StudentDocsAdmin(admin.ModelAdmin):
    form = StudentDocsForm
    #fields = ('Number','Date')
    fields = (
        'SeriaNumDoc',
        'DatarRegDoc',
    )
#
'''
'''
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    fields = (
        'Name',
        'DateBirth',
        'Group'
    )
    #inlines = [GenderInline, StudentDocsInline]
#
'''
@admin.register(EducationForm)
class EducationFormAdmin(admin.ModelAdmin):
    form = EducationFormForm
    #fields = ('Number','Date')
    fields = (
        'EducationForm',
    )
#
@admin.register(SuddopConstants)
class SuddopConstantsAdmin(admin.ModelAdmin):
    form = SuddopConstantsForm
    fields = (
        'SConstName',
        'SConstValue',
        'SConstDescription',
    )
