from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/success')
def success():
    paymentKey = request.args.get('paymentKey', "")
    orderId = request.args.get('orderId', "")
    amount = request.args.get('amount', "")

    url = "https://api.tosspayments.com/v1/payments/"+paymentKey
    params = {'orderId': orderId, 'amount': amount}
    headers = {'Authorization': 'Basic dGVzdF9za19aMFJuWVgydzUzMkVtbnpZWGpSOE5leXFBcFFFOg==',
               'Content-Type': 'application/json'}
    res = requests.post(url, data=json.dumps(params), headers=headers)

    print('## URL : ', res.request.url)
    print('## 요청헤더 : ', res.request.headers)
    print('## 요청보디 : ', res.request.body)
    print('## 요청결과 : ', res.text)

    return render_template('success.html', result=res.json())