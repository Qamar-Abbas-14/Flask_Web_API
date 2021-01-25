
class PaymentGateway():
    def __init__(self, data):
        self.service=None
        self.data=data
        print(f"Method is {self.service}")

class CheapPaymentGateway(PaymentGateway):
    def __init__(self, data):
        self.service="CheapPaymentGateway"
        self.data=data
        print(f"Method is {self.service}")

class ExpensivePaymentGateway(PaymentGateway):
    def __init__(self, data):
        self.service="ExpensivePaymentGateway"
        self.data=data
        print(f"Method is {self.service}")

class PremiumPaymentGateway(PaymentGateway):
    def __init__(self, data):
        self.service="PremiumPaymentGateway"
        self.data=data
        print(f"Method is {self.service}")


class MakePayment():
    def __init__(self, data):
        self.data = data
        self.AMT=data['AMT']

    def select_payment_gateway(self):
        if self.AMT>0 and self.AMT<=20:
            try:
                payment_service =  CheapPaymentGateway(self.data)
                return "<h2>Payment is processed: 200 OK</h2>",200      
            except:
                print("Payment Could not be Processed by CheapPaymentGateway ..")
                return "500 Internal server error", 500
        elif self.AMT>20 and self.AMT<=500:  
            try:
                payment_service =  ExpensivePaymentGateway(self.data)
                return "<h2>Payment is processed: 200 OK</h2>", 200
            except:
                try:
                    payment_service =  CheapPaymentGateway(self.data)
                    return "<h2>Payment is processed: 200 OK</h2>", 200
                except:
                    print("Payment Could not be Processed by ExpensivePaymentGateway & CheapPaymentGateway ..")
                    return "500 Internal server error", 500
        elif self.AMT>500:
            tried=0
            while (tried<3):
                try:
                    payment_service =  PremiumPaymentGateway(self.data)
                    return "<h2>Payment is processed: 200 OK</h2>", 200
                except:
                    tried=tried+1
                    print("Payment Could not be Processed by PremiumPaymentGateway in try %s.."%(tried))
            
            return "500 Internal server error", 500
        else:
            return "<h2>The request is invalid: 400 bad request</h2>", 400






