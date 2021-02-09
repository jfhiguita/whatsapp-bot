from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/")
def hello():
    return "Whatsapp Bot"


@app.route("/sms", methods=['POST'])
def sms():
    msg = request.form.get('Body')

    #create reply
    resp = MessagingResponse()
    resp.message(f"You said: {msg}")

    return str(resp)


#if __name__ == "__main__":
    #app.run(debug=True)

