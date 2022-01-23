import os
from twilio.rest import Client

# if you have a Twilio account, insert your SID and Auth Token here
# authors' personal credentials have replaced
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

client.messages.create(
                     body="https://www.figma.com/proto/dosS0tkqBeAAKR0OUs4Zht/SOURDOE?node-id=3%3A142&scaling=scale-down&page-id=0%3A1&starting-point-node-id=2%3A2",
                     from_= '+19592144471',
                     to= os.environ.get('CELL_PHONE_NUMBER')
                 )

