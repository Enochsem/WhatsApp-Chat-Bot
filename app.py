# from flask import Flask, request
from flask import *
# import os
from twilio.twiml.messaging_response import MessagingResponse
from dialogflow_file import dialog_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


# call back url
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message"""
    # fetch the msg
    msg = request.form.get('Body')
    
    phone_number = request.form.get('From')
    
    reply = dialog_reply(msg, phone_number)
    
    # create reply
    resp = MessagingResponse()
    resp.message(reply)
    # resp.message("you said: {}".format(msg))
    # pass reply into resp.message

    return str(resp)

if  __name__ == "__main__":
    app.run(debug=True)

   
    # port = os.environ.get('PORT',5000)
    # app.run(debug=True, host='0.0.0.0',port=port)