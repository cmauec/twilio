from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/whatsapp', methods=['GET', 'POST'])
def send_whatsapp():
    """
    Send message to whatsapp
    """
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body='Otra prueba 😊',
                                from_='whatsapp:+',
                                to='whatsapp:'
                            )

    return message.sid


@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    # resp = MessagingResponse()
    body1 =  request.form['Body']

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body=body1,
                                from_='whatsapp:+',
                                to='whatsapp:+'
                            )

    # Add a message
    # resp.message(body)

    # return str(resp)
    return message.sid


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
