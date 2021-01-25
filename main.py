from flask import Flask,abort, request
from verfiications import Card_Verifications
from payment_gateways import select_payment_gateway
import requests
import json
import pdb




app=Flask(__name__)

@app.route('/ProcessPayment/', methods=['GET'])
def ProcessPayment():
    if request.method == 'GET':
        req_data=request.get_data()
        if req_data:
            data=json.loads(req_data)
        else:
            return "<h2>The request is invalid: 400 bad request</h2>", 400

        print(data)
        card=Card_Verifications()
        validity=card.verify(data)
        print("Complete Validity is :",validity)

        if validity:
            print("Proceeding for payment methods")
            amount=data['AMT']
            obj=select_payment_gateway(data)
            msg, code =obj.MakePayment()
            print(msg,code)
            return msg, code

        else:
            return "<h2>The request is invalid: 400 bad request</h2>", 400
    else:
        return "<h2>The request is invalid: 400 bad request</h2>", 400



if __name__=='__main__':
    app.run(debug=True)