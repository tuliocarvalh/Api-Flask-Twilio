from operator import index
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import time
import os


account_sid = '' 
auth_token = ''

def fun_teste() :
    os.system("start Chrome.exe")




app = Flask(__name__)

@app.route('/bot', methods=['POST'])


def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'ola' in incoming_msg:
        msg.body('Ola, em que posso ajudar?')
        responded = True

    if 'funcao teste' in incoming_msg:
        fun_teste()
        msg.body('Tarefa executada com sucesso.')
        responded = True

    if responded:
       return str(resp)

    if not responded:
        msg.body('Não compreendi. Desculpe.')
        return str(resp)


if __name__ == '__main__':
    app.run()