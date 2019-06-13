# tasks.py
import logging
import time
import os
from django.urls import reverse
from celery import Celery
from celery import task
from celery import app
from .models import *
from celery.utils.log import get_task_logger
#
import logging
import sys
import smpplib.gsm
import smpplib.client
import smpplib.consts
from threading import Thread
import time
#
import base64
import quopri
import smtplib, ssl
import email.message
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#
@task
def send_sms_sign(phone_number, contract_sign_message, userzign, sms_code):
#
    logger = logging.getLogger('django')
    logging.basicConfig(level='DEBUG')
    parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(contract_sign_message)
    client = smpplib.client.Client('10.236.22.177', '12000')
    client.connect()
    client.bind_transceiver(system_id='MSK_vrbvgr', password='m03P7nLB')
    for part in parts:
        pdu = client.send_message(
            source_addr_ton=smpplib.consts.SMPP_TON_INTL,
            #source_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            # Make sure it is a byte string, not unicode:
            source_addr='GBPOU_VG',
            dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
            #dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            # Make sure thease two params are byte strings, not unicode:
            #destination_addr='79169122979',
            destination_addr=phone_number,
            short_message=part,
            data_coding=encoding_flag,
            esm_class=msg_type_flag,
            registered_delivery=True,
        )
    cs = ContractSign.objects.get(SignKey = userzign)
    cs.SmsCode = sms_code
    cs.save()
    client.unbind()
    client.disconnect()
#

@task
def send_mail_sign(applicant_email, contract_number, contract_id, applicant_fullname, csc):
#
    def contains_non_ascii_characters(str):
        return not all(ord(c) < 128 for c in str)
#
    def add_header(message, header_name, header_value):
        if contains_non_ascii_characters(header_value):
            h = Header(header_value, 'utf-8')
            message[header_name] = h
        else:
            message[header_name] = header_value
        return message
#
    try:
        #smtp_server = "m.dvorec.net"
        smtp_server = "mail.dvorec.net"
        port = 587
        #sender_email = "esz@m.dvorec.net"
        sender_email = "esz@dvorec.net"
        sender_email_header = "esz@mailvg.ru"
        mail_subject = 'Подписать договор'
        #sender_name = 'Vorobyovi Gory'
        sender_name = 'ГБПОУ "Воробьёвы горы"'
        message = 'Это сообщение'
        From = '%s <%s>' % (sender_name, sender_email_header)
        reciver_email = applicant_email
        #password = "2J6F5zoQ8RwT"
        password = "MHo97dFJWZsdEXmuw5GE"
        # Create a secure SSL context
        context = ssl.create_default_context()
        # Try to log in to server and send email
        server = smtplib.SMTP(smtp_server,port,timeout=10)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        msg = MIMEMultipart()
        msg['Subject'] =  Header(mail_subject)
        msg['From'] =  Header(From)
        msg['To'] =  Header(reciver_email)
        #html = '<a href="%s">%s</a>' % ('http://dev.esz.dvorec.net/smssign/' + csc, 'http://dev.esz.dvorec.net/smssign/' + csc)
        ContractLink = 'http://demo.contract.dvorec.net/smssign/' + csc
        #html_email_tmpl =  os.path.join(PROJECT_ROOT, 'templates/smssign/email/email_sign.html')
        html_email_tmpl =  '/var/www/html/esz/templates/smssign/email/email_sign.html'
        with open(html_email_tmpl, 'r') as file:
            html = file.read().replace('\n', '')
            html = html.replace('ContractId', contract_number)
            html = html.replace('ContractLink', ContractLink)
            html = html.replace('applicantFullname', applicant_fullname)

        if contains_non_ascii_characters(html):
            html_text = MIMEText(html.encode('utf-8'), 'html','utf-8')
        else:
            html_text = MIMEText(html, 'html')
        msg.attach(html_text)
        server.sendmail(sender_email, reciver_email, msg.as_string())
        cstrs = ContractSignTransaction.objects.get(Contract = Contract.objects.get(id = contract_id))
        cstrs.ContractSignTransactionState = ContractSignTransactionState.objects.get(id=98)
        cstrs.save()
    except Exception as e:
        logger.info(e)
        print(e)
        logger.info("Task error")
    finally:
        server.quit()
