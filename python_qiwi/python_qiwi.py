
import requests
import time
import random
import string


class QiwiWаllet():

    def __init__(self, phone, api_token):
        """init

        Args:
            phone (str): wallet phone number
            api_token (str): qiwi.com/api token
        """

        self.s = requests.Session()
        self.s.headers['authorization'] = 'Bearer ' + api_token
        self.phone = phone

    def pay(self, to_qw: str, sum_p2p: int, comment='', currency=643):
        """pay

        Args:
            to_qw (str): wallet number for transfer
            sum_p2p (int): transfer amount in int format
            comment (str, optional): payment comment. Defaults to ''.
            currency (int, optional): currency code (by default - ruble). Defaults to 643.

        Returns:
            json: information about the success of the translation
        """

        sum_p2p = str(int(sum_p2p)) + '.00'
        self.s.headers = {
            'content-type': 'application/json',
            'User-Agent': 'Android v3.2.0 MKT',
            'Accept': 'application/json',
        }

        postjson = {"id": str(int(time.time() * 1000)), "sum": {
            "amount": sum_p2p, "currency": str(currency)
        }, "paymentMethod": {
            "type": "Account", "accountId": str(currency)
        }, "comment": str(comment), "fields": {"account": to_qw}}
        res = self.s.post(
            'https://edge.qiwi.com/sinap/api/v2/terms/99/payments',
            json=postjson)
        return res.json()

    def payment_history(self, rows_num=5):
        """payment_history

        Args:
            rows_num (int, optional): the number of payments you want to receive. Defaults to 5.

        Returns:
            json: payment_history
        """

        parameters = {'rows': str(
            rows_num), 'nextTxnId': '', 'nextTxnDate': ''}
        h = self.s.get('https://edge.qiwi.com/payment-history/v2/persons/' +
                       self.phone + '/payments', params=parameters)
        return h.json()

    def bill(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(12))

    def check(self, comment):
        """check_payment

        Args:
            comment (str): desthis is a special combination of characters specified during translationcription

        Returns:
            bool: was the payment found
        """

        lastPayments = self.payment_history(40)
        for payment in lastPayments:
            qcomment = payment['comment']
            if comment in qcomment:
                return True
        return False

    def full_balance(self):
        """get full balance

        Returns:
            json: complete information about your accounts
        """

        self.s.headers['Accept'] = 'application/json'

        b = self.s.get(
            'https://edge.qiwi.com/funding-sources/v2/persons/' + self.phone +
            '/accounts')
        return b.json()

    def balance(self):
        """get balance

        Returns:
            json: balance of your first account
        """
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

    def get_payment(self, comment):
        """get payment

        Args:
            comment (str): special combination of characters

        Returns:
            json: payment info
        """        
        lastPayments = self.payment_history(30)
        for payment in lastPayments:
            qcomment = payment['comment']
            if comment in qcomment:
                return payment
        return False
