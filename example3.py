class Paymentprocessor:
    def process_payment(self,amount):
        raise NotImplementedError("subclasses should implement this method!")
class creditcardprocessor(Paymentprocessor):
    def process_payment(self, amount):
        return f"processing credit card payment of {amount}."

class Paypalprocesser(Paymentprocessor):
    def process_payment(self,amount):
        return f"processing paypal payment of {amount}."
class Banktransferprocessor(Paymentprocessor):
    def process_payment(self, amount):
        return f"processing bank transfer of {amount}"

def process_payments(processors, amount):
        for processor  in processors:
            print(processor.process_payment(amount))

processors= [creditcardprocessor(),Paypalprocesser(),Banktransferprocessor()]

process_payments(processors, 100)
