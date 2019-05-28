import logging
import sys
import smpplib.gsm
import smpplib.client
import smpplib.consts
from threading import Thread
import time


class custom_client(smpplib.client.Client):
    """1"""
    msg_delevered = False
    msg_sent = False
#
    def listen(self, ignore_error_codes=None):
        """Listen for PDUs and act"""
        while not self.msg_delevered:
            self.read_once(ignore_error_codes)

#
    def set_message_received_handler(self, func):
        """Set new function to handle message receive event"""
        ss = SendSmsTransactionState(id=5, SatateLabel='DELEV')
        ss.save()
        self.msg_delevered = True
        #self.message_received_handler = func
#
    def set_message_sent_handler(self, func):
        ss = SendSmsTransactionState(id=6, SatateLabel='Sent')
        ss.save()
        self.msg_sent = True
        """Set new function to handle message sent event"""
        #self.message_sent_handler = func
#
def send_sms(phone_number, message):
    logging.basicConfig(level='DEBUG')
    parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(message)
    client = custom_client('10.236.22.177', '12000')
    # Print when obtain message_id
    client.set_message_sent_handler(
        lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))
    client.set_message_received_handler(
        lambda pdu: sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id)))
    # Print when obtain message_id
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
            #print(pdu.sequence)
            #
    client.listen()
    client.unbind()
    time.sleep(5)
    client.disconnect()
#
send_sms('79096510789', u'Teat\n')
