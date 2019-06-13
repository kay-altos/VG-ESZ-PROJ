from django.shortcuts import render
from django.http import HttpResponse
from suddop.models import *
from staicsitecontent.models import *
from suddop.tasks import send_sms_sign, send_mail_sign
import random
import json
from django.http import JsonResponse
from django.utils.html import format_html
import pdfkit
from django.template.defaultfilters import date as _date
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

#

'''
class Center(models.Model):
    Name = models.CharField(max_length=250, verbose_name="Название центра")
    ShortName = models.CharField(max_length=100, verbose_name="Краткое название центра")
    Description = models.TextField(max_length=2048,verbose_name="Описание")
    Code = models.CharField(max_length=30,verbose_name="Код")
    Address = models.TextField(max_length=100,verbose_name="Адрес")
'''



class ContractView(APIView):
    def get(self, request, userzign):
        ContractSignObj = ContractSign.objects.get(SignKey = userzign)
        center = Center.objects.get(pk = str(ContractSignObj.Contract.Program.Center.id))
        contract = Contract.objects.get(pk = ContractSignObj.Contract.pk)
        ApplicantPhone = ApplicantPhones.objects.get(Applicant = ContractSignObj.Contract.Applicant)
        ApplicantEmail = ApplicantEmails.objects.get(Applicant = ContractSignObj.Contract.Applicant)
        ApplicantPassp = ApplicantPassport.objects.get(Applicant = ContractSignObj.Contract.Applicant)
        PageGreet = SuddopConstants.objects.get(SConstName = 'sms_sign_page_greeting')
        CentSerializer =  CenterSerializer(center, many=False)
        SerializerContract = ContractSerializer(ContractSignObj.Contract, many=False)
        ApplicantPhoneSerializer = ApplicantPhonesSerializer(ApplicantPhone, many=False)
        ApplicantEmailSerializer = ApplicantEmailsSerializer(ApplicantEmail, many=False)
        ApplicantPasspSerializer = ApplicantPassportSerializer(ApplicantPassp, many=False)
        PageGreetSerializer = PageGreetingSerializer(PageGreet, many=False)
        return Response({
            "Contract": SerializerContract.data,
            "ApplicantPhone" : ApplicantPhoneSerializer.data,
            "ApplicantEmail" : ApplicantEmailSerializer.data,
            "ApplicantPassp" : ApplicantPasspSerializer.data,
            "PageGreet" : PageGreetSerializer.data,
            "Center" : CentSerializer.data,

        })

# Create your views here.
def smssign(request, userzign):
    ContractSignObj = ContractSign.objects.get(SignKey = userzign)
    csitr = ContractSignTransaction.objects.get(Contract = ContractSignObj.Contract)
    ApplicantEmail = ApplicantEmails.objects.get(Applicant = ContractSignObj.Contract.Applicant)
    ApplicantPhone = ApplicantPhones.objects.get(Applicant = ContractSignObj.Contract.Applicant)
    ApplicantPassp = ApplicantPassport.objects.get(Applicant = ContractSignObj.Contract.Applicant)
    page_greeting = SuddopConstants.objects.get(SConstName = 'sms_sign_page_greeting')
    cce_group = Group.objects.get(Program = ContractSignObj.Contract.Program)
    #
    def contract_form_generate():
        c_templ = ContractTemplates.objects.get(id = '1')
        student_Birth = ContractSignObj.Contract.Student.DateBirth
        new_data = c_templ.templ
        c_templ_tags = {
            '*contr_number*': ContractSignObj.Contract.Number,
            '*applicant_fullName*': ContractSignObj.Contract.Applicant.FullName,
            '*organization_pred*': "Мельвель Елены Хасыновны",
            '*organization_pred_prikaz*': "Приказ № 123564",
            '*contr_applicant_gender_postfix*': "ый",
            '*contr_student_gender_postfix*': "ый",
            '*student_fullname*': ContractSignObj.Contract.Student.Name,
            '*applicant_psp_serial*': ApplicantPassp.SerialPaspDoc,
            '*applicant_psp_num*': ApplicantPassp.NumPaspDoc,
            '*applicant_psp_DataOut*': _date(ApplicantPassp.DataOutDoc, "«d» E Y г."),
            '*student_Birth*': _date(ContractSignObj.Contract.Student.DateBirth, "«d» E Y г."),
            '*applicant_psp_WhomWhenIssue*': ApplicantPassp.ApplicantDocWhomWhenIssued,
            '*applicant_psp_address*': ApplicantPassp.ApplicantAddress,
            '*student_sn*': ContractSignObj.Contract.Student.SeriaNumDoc,
            '*contr_program*': ContractSignObj.Contract.Program.Name,
            '*contr_date*': _date(ContractSignObj.Contract.Date, "«d» E Y г.")
        }
#
        for key, val in c_templ_tags.items():
            tmp = new_data
            new_data = tmp.replace(key, val)

        contr_name = '/var/www/html/esz/esz/static/tmpls/htmltplcontracts/%s.html' % (userzign)
        with open (contr_name, 'w') as f: f.write(new_data)
        #pdfkit.from_url('/var/www/html/esz/esz/static/tmpls/htmltplcontracts/%s.html' % (userzign), '/var/www/html/esz/esz/static/tmpls/out.pdf')
        '''with open ('/var/www/html/esz/esz/static/tmpls/contr_tpl.mht', 'w') as f: f.write(new_data)
        pdfkit.from_url('/var/www/html/esz/esz/static/tmpls/contr_tpl.mhtl', '/var/www/html/esz/esz/static/tmpls/out.pdf')'''
#

    #contract_form_generate()
#
    if request.method == 'GET':
        if csitr.ContractSignTransactionState == ContractSignTransactionState.objects.get(id=98):
            '''новый договор'''
            csitr.ContractSignTransactionState = ContractSignTransactionState.objects.get(id=1)
            csitr.save()
#
    data = {
            'userzign' : userzign,
    }
#
    if request.method == 'POST' and request.is_ajax():
        '''post запрос в режиме ajax'''
        body_unicode = request.body.decode('utf-8')
        '''приобразуем сырой запрос к utf-8'''
        body = json.loads(body_unicode)
        '''извлекаем json в dic'''
        content = body['data']
        model_contract = Contract.objects.get(pk = content['Contract']['id'])
        model_applicant = Applicant.objects.get(pk = content['Contract']['applicant']['id'])
        model_ApplicantPhone = ApplicantPhones.objects.get(Applicant = content['ApplicantPhone']['Applicant'])


        applicant_serializer = ApplicantSerializer(model_applicant, data=content['Contract']['applicant'])
        serializer_ApplicantPhone = ApplicantPhonesSerializer(model_ApplicantPhone, data=content['ApplicantPhone'])
        if serializer_ApplicantPhone.is_valid():
            serializer_ApplicantPhone.save()

        if applicant_serializer.is_valid():
            applicant_serializer.save()
            #contract_form_generate()
            return JsonResponse({'result': applicant_serializer.data})

    return render(request, "smssign/emailsign.html", context=data)
