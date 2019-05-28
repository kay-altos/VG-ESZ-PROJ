from django.shortcuts import render
from django.http import HttpResponse
from suddop.models import *
from suddop.tasks import send_sms_sign, send_mail_sign
import random
import json
from django.http import JsonResponse
from django.utils.html import format_html
# Create your views here.
def smssign(request, userzign):
    ContractSignObj = ContractSign.objects.get(SignKey = userzign)
    csitr = ContractSignTransaction.objects.get(Contract = ContractSignObj.Contract)
    ApplicantEmail = ApplicantEmails.objects.get(Applicant = ContractSignObj.Contract.Applicant)
    ApplicantPhone = ApplicantPhones.objects.get(Applicant = ContractSignObj.Contract.Applicant)
    ApplicantPassp = ApplicantPassport.objects.get(Applicant = ContractSignObj.Contract.Applicant)
    page_greeting = SuddopConstants.objects.get(SConstName = 'sms_sign_page_greeting')
    cce_group = Group.objects.get(Program = ContractSignObj.Contract.Program)
    c_templ = ContractTemplates.objects.get(id = '1')

    new_data = c_templ.templ.replace('*contr_number*', ContractSignObj.Contract.Number)
    new_data = new_data.replace('*applicant_fullName*', ContractSignObj.Contract.Applicant.FullName)
    with open ('/var/www/html/esz/esz/static/tmpls/contract_vn_08_04_2019-3.html', 'w') as f:
        f.write(new_data)

#
    if request.method == 'GET':
        if csitr.ContractSignTransactionState == ContractSignTransactionState.objects.get(id=98):
            '''новый договор'''
            csitr.ContractSignTransactionState = ContractSignTransactionState.objects.get(id=1)
            csitr.save()
#
    data = {
            'userzign' : userzign,
            'page_greeting' : format_html(page_greeting.SConstValue),
            'cce_program' : ContractSignObj.Contract.Program,
            'cce_group' : cce_group,
            'cce_stud' : ContractSignObj.Contract.Student,
            'ContractObj' : ContractSignObj,
            'ApplicantEmail' : ApplicantEmail,
            'ApplicantPhone' : ApplicantPhone,
            'ApplicantPassp' : ApplicantPassp,
            'SmsCode' : ContractSignObj.SmsCode,
            #'c_templ' : format_html(c_templ.templ),
            'ContractSignTransactionState' : csitr.ContractSignTransactionState
    }
#
    if request.method == 'POST' and request.is_ajax():
        '''post запрос в режиме ajax'''
        body_unicode = request.body.decode('utf-8')
        '''приобразуем сырой запрос к utf-8'''
        body = json.loads(body_unicode)
        '''извлекаем json в dic'''
        content = body['action']
        if content == 'saveApplicantPasport':
            applct = Applicant.objects.get(id = ContractSignObj.Contract.Applicant.id)
            applct.FullName = body['FullName']
            applct.ApplicantEmail = body['ApplicantEmail']
            applct.ApplicantPhone = body['ApplicantPhone']
            ApplicantPassp.ApplicantDocWhomWhenIssued = body['ApplicantDocWhomWhenIssued']
            ApplicantPassp.ApplicantAddress = body['ApplicantAddress']
            ApplicantPassp.SerialPaspDoc = body['SerialPaspDoc']
            ApplicantPassp.NumPaspDoc = body['NumPaspDoc']
            ApplicantPassp.DataOutDoc = body['DataOutDoc']
            applct.ApplicantSnils = body['ApplicantSnils']
            applct.save()
            ApplicantPassp.save()
            return JsonResponse({'oooo': '111'})
        if content == 'saveStudent':
            stdnt = Student.objects.get(id = ContractSignObj.Contract.Student.id)
            stdnt.Name = body['Name']
            stdnt.DateBirth = body['DateBirth']
            stdnt.DocumentType = body['DocumentType']
            stdnt.SeriaNumDoc = body['SeriaNumDoc']
            stdnt.DatarRegDoc = body['DatarRegDoc']
            stdnt.GenderLabel = body['GenderLabel']
            stdnt.save()
            return JsonResponse({'oooo': '111'})
        if content == 'SendSmsSign':
            cstrst = ContractSignTransactionState.objects.get(id=2)
            csitr.ContractSignTransactionState =  cstrst
            csitr.save()
            rnd = random.randint(1000,9999)
            msg = 'Для подписания договора № %s, используйте код: %s' % (ContractSignObj.Contract.Number, rnd)
            send_sms_sign.delay(ApplicantPhone.Phone, msg, userzign, rnd)
            return JsonResponse({'csts_id': cstrst.id, 'csts_lable' : cstrst.SatateLabel})
        elif content == 'verifyCode':
            if ContractSignObj.SmsCode == body['vsmsCode']:
                Contr =  Contract.objects.get(id=ContractSignObj.Contract.id)
                Contr.ContractStatus = ContractStatus.objects.get(id=2)
                Contr.save()
                cstrst = ContractSignTransactionState.objects.get(id=3)
                csitr.ContractSignTransactionState = cstrst
                csitr.save()
                return JsonResponse({'csts_id': cstrst.id, 'csts_lable' : cstrst.SatateLabel})
            else:
                pass
    return render(request, "smssign/emailsign.html", context=data)
