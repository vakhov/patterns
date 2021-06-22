from futures.strategy.interfaces import PaymentStrategy


class PayPalPaymentStrategy(PaymentStrategy):
    def pay(self, data: dict):
        # work with data
        print('work with paypal API')
        print(data)
        return True


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, data: dict):
        # work with data
        print('work with Bank api')
        print(data)
        return True


class WebMoneyPaymentStrategy(PaymentStrategy):
    def pay(self, data: dict):
        # work with data
        print('work with WebMoney api')
        print(data)
        return True
