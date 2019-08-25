from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    if msg == "!rules":
        resp.message(" 1.https://www.youtube.com/channel/UC3K6YcpEvJRgpnloGVtj1LQ plz subscribe like and share  2.Dont ask for gender of ur fish Basic requirements for fh tank : https://youtu.be/ar2w58yoohc 3.Sales post only allowed for verified sellers saroj,vasant,pranjal,jayesh,krn shirke,rehman,kaif,prisha,Dan,gnanesh,jaiveer,Pranav pandav No politicals post no fwd msgs or links")

    elif msg =="!help":
        resp.message("1>for rules type *!rules"
                    "2>for facebook link type *!fb"
                    "3>for youtube link type *!yt"
                    "4>for website link type *!website"
                    "5> for event dates type *!events")
    
    elif msg =="!fb":
        resp.message("https://www.facebook.com/groups/268765800702283/")

    elif msg =="!yt":
        resp.message("https://www.youtube.com/channel/UC3K6YcpEvJRgpnloGVtj1LQ")
        

    else:
        resp.message("You said: {}".format(msg))


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)