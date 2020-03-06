from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Chat-Bot"

# call back url
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message"""
    # fetch the msg
    msg = request.form.get('Body')
    # create reply
    resp = MessagingResponse()
    resp.message("you said: {}".format(msg))

    return str(resp)

if  __name__ == "__main__":
    app.run(debug=True)