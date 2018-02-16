from flask import Flask,request
import random

from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAbt8KW5n7MBAIZCdH6sKrRVgdDm0CZAGB0DDQlLBDmmqIyDqZCtZClLUabfpRkP2ipiRo1bzxbJtKltmg7D48T2bire6TEPVI8J1J6V0Mt6JguYX3GHTRnlnbEKQZC0xyusMAy3LWW4ZCKmhxsGwvnrrsGdB5tS5tDeXANSqoGtE9LD2ra3Fh'
VERIFY_TOKEN = 'EAAbt8KW5n7MBAIZCdH6sKrRVgdDm0CZAGB0DDQlLBDmmqIyDqZCtZClLUabfpRkP2ipiRo1bzxbJtKltmg7D48T2bire6TEPVI8J1J6V0Mt6JguYX3GHTRnlnbEKQZC0xyusMAy3LWW4ZCKmhxsGwvnrrsGdB5tS5tDeXANSqoGtE9LD2ra3Fh'
bot = Bot(ACCESS_TOKEN)


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    output = request.json
    print(output)
    if request.method == 'GET':
        if request.args.get("hub.verify_token")==ACCESS_TOKEN :
            return request.args.get("hub.challenge")
    else:
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        print message['message'].get('text')
                        response_sent_text ="Thank You for contacting we will connect with you soon"
                        bot.send_text_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = "We're greatful to know you :)"
                        bot.send_text_message(recipient_id, response_sent_nontext)
    return "Message Processed"
 
 
if __name__ == '__main__':
    app.run()