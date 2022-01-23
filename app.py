import os
from flask import Flask, request, redirect, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def home():
    resp = MessagingResponse()
    resp.message("https://www.figma.com/proto/dosS0tkqBeAAKR0OUs4Zht/SOURDOE?node-id=3%3A142&scaling=scale-down&page-id=0%3A1&starting-point-node-id=2%3A2")
    return str(resp)

if __name__ == '__main__':
    app.run()
