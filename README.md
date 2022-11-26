# python-qiwi
## **RU** version
### Библиотека python-qiwi используется для удобной работы с api QIWI кошелька
____

### Установка:
```pip install - U python-qiwi```

### Создание объекта wallet:
```python
import python_qiwi
phone = '+79021234567' # номер телефона
token = 'token' # токен полученный на сайте https://qiwi.com/api
wallet = python_qiwi.QiwiWаllet(phone, token)
```
### Получение баланса кошелька

```python
wallet.balance()
```
Это вернёт баланс первого вашего счёта. Например: 500.00


Если же вы хотите получить баланс со всех свох счетов то используйте
```python
wallet.full_balance()
```
Это вернёт вам json ответ. Например:
```json
{'accounts': [{'alias': 'qw_wallet_rub', 'fsAlias': 'qb_wallet', 'bankAlias': 'QIWI', 'title': 'Qiwi Account', 'type': {'id': 'WALLET', 'title': 'QIWI Wallet'}, 'hasBalance': True, 'balance': {'amount': 500.00, 'currency': 643}, 'currency': 643, 'defaultAccount': True}]}
```
____

### Платёж
Для того чтобы перевести деньги с кошелька на кошелёк используйте
```python
wallet.pay(to_qw='+79012345678', sum_p2p=10, comment='комментарий к платежу', currency=643)
```
to_qw - номер кошелька для перевода

sum_p2p -  сумма перевода в формате int

comment - комментарий к платежу

currency - код валюты(по умолчанию - рубль)
___
### Выставление счёта
Испоьзуйте
```python
bill = wallet.bill()
```
Вы получите специальную комбинацию символов. Её надо указать при переводе средств на счёт указанный при создании объекта кошелька
____
### Проверка оплаты
Для того что бы проверить оплату используйте
```python
if wallet.check(bill):
    print('Оплата прошла')
```
bill - это специальная комбинация символов. Вы могли получить её в [прошлом разделе](###Выставление-счёта)
___
### Получение информации о платеже
```python
wallet.get_payment(bill)
```
bill - это специальная комбинация символов. Вы могли получить её в разделе ["Выставление счёта"](###Выставление-счёта)
____
### Получение истории платежей
```python
wallet.payment_history(rows_num=10)
```
rows_num - количество платежей которые вы хотите получить
____
### Получение информации о профиле
```python
wallet.get_profile()
```
Вернёт информацию о профиле
