from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False

    if 'hello' in incoming_msg:
        msg.body('Hi there! How can I help you today?')
        responded = True
    elif 'bye' in incoming_msg:
        msg.body('Goodbye! Have a great day!')
        responded = True

    if not responded:
        msg.body('I only understand "hello" and "bye" for now.')

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
