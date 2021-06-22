from typing import Optional, Dict

from futures.strategy.interfaces import PaymentStrategy
from futures.strategy.strategy import (
    PayPalPaymentStrategy, WebMoneyPaymentStrategy, CreditCardPaymentStrategy
)


class Order:
    def pay(self, data: dict, payment_strategy: PaymentStrategy):
        payment_strategy.pay(data=data)


if __name__ == '__main__':
    o = Order()
    payment_method = input('How do you want to pay, with PayPal, CreditCard or WebMoney (enter pp, cc, wm)?: ')
    payment_strategy: Optional[PaymentStrategy] = None
    data: Optional[Dict] = None
    if payment_method == 'pp':
        pay_pal_email = input('Enter PayPal email: ')
        data = dict(
            method='paypal',
            email=pay_pal_email
        )
        payment_strategy = PayPalPaymentStrategy()
    elif payment_method == 'wm':
        vm_number = input('Enter WebMoney number: ')
        data = dict(
            method='webmoney',
            number=vm_number
        )
        payment_strategy = WebMoneyPaymentStrategy()
    elif payment_method == 'cc':
        cc_number = input('Enter Credit card number: ')
        cc_date = input('Enter credit card expiration date: ')
        cc_owner = input('Enter Credit card owner: ')
        data = dict(
            method='creditcard',
            number=cc_number,
            date=cc_date,
            owner=cc_owner
        )
        payment_strategy = CreditCardPaymentStrategy()
    else:
        exit('Wrong payment method, you have to enter: pp, cc, wm')

    o.pay(data=data, payment_strategy=payment_strategy)
