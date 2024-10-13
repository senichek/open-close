from abc import ABC, abstractmethod

class PaymentService(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPaymentService(PaymentService):
    def process_payment(self):
        print("Processing credit card payment")


class PayPalPaymentService(PaymentService):
    def process_payment(self):
        print("Processing PayPal payment")


class ApplePayPaymentService(PaymentService):
    def process_payment(self):
        print("Processing Apple payment")


# Payment service registry
payment_service_registry = {}

def register_payment_service(payment_method: str, service_class):
    payment_service_registry[payment_method] = service_class

# Register services
register_payment_service("credit_card", CreditCardPaymentService)
register_payment_service("paypal", PayPalPaymentService)
register_payment_service("apple_pay", ApplePayPaymentService)
