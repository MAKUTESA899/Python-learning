from twilio.rest import Client
from flask import Flask, request, jsonify

app = Flask(__name__)

# Your Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
whatsapp_from = 'whatsapp:+14155238886'  # Twilio WhatsApp sandbox number
whatsapp_to = 'whatsapp:your_whatsapp_number'  # Your WhatsApp number

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Define routes for incoming messages
@app.route('/incoming', methods=['POST'])
def incoming_message():
    data = request.get_json()
    message_body = data['Body']
    sender = data['From']

    # Process the incoming message
    response = process_message(message_body)

    # Send response
    send_message(sender, response)

    return jsonify({'success': True})

# Process incoming messages
def process_message(message):
    # Here you can define your bot logic
    # For example, you could have a simple echo bot
    return "You said: " + message

# Send message
def send_message(recipient, message):
    client.messages.create(
        from_=whatsapp_from,
        body=message,
        to=recipient
    )

if __name__ == '__main__':
    app.run(debug=True)
