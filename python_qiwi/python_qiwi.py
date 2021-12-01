
import requests
import time
import random
import string


class QiwiWwаllet():

    def __init__(self, phone, api_token):
        self.s = requests.Session()
        self.s.headers['authorization'] = 'Bearer ' + api_token
        self.phone = phone

    def pay(self, to_qw, sum_p2p, comment=''):
        sum_p2p = str(int(sum_p2p)) + '.00'
        self.s.headers = {
            'content-type': 'application/json',
            'User-Agent': 'Android v3.2.0 MKT',
            'Accept': 'application/json',
        }

        postjson = {"id": str(int(time.time() * 1000)), "sum": {
            "amount": '2.00', "currency": "643"
        }, "paymentMethod": {
            "type": "Account", "accountId": "643"
        }, "comment": str(comment), "fields": {"account": to_qw}}
        res = self.s.post(
            'https://edge.qiwi.com/sinap/api/v2/terms/99/payments',
            json=postjson)
        return res.json()

    def payment_history(self, rows_num=5):
        parameters = {'rows': str(rows_num), 'nextTxnId': '', 'nextTxnDate': ''}
        h = self.s.get('https://edge.qiwi.com/payment-history/v2/persons/' +
                       self.phone + '/payments', params=parameters)
        return h.json()

    def bill(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(7))

    def check(self, comment):
        lastPayments = self.payment_history(20)
        for payment in lastPayments:
            qcomment = payment['comment']
            if comment in qcomment:
                return True
        return False

    def full_balance(self):

        self.s.headers['Accept'] = 'application/json'

        b = self.s.get(
            'https://edge.qiwi.com/funding-sources/v2/persons/' + self.phone +
            '/accounts')
        return b.json()

    def balance(self):
        self.s.headers['Accept'] = 'application/json'

        b = self.s.get(
            'https://edge.qiwi.com/funding-sources/v2/persons/' + self.phone + '/accounts')
        b = b.json()
        b = b['accounts'][0]['balance']['amount']

        return b

    def get_profile(self):

        self.s.headers['Accept'] = 'application/json'

        p = self.s.get(
            'https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true')
        return p.json()
