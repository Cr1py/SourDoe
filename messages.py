import os
from twilio.rest import Client

# if you have a Twilio account, insert your SID and Auth Token here
# authors' personal credentials have replaced
account_sid = 'AC993851487540e81bb6a879b9f2a085f7'
auth_token = '6b43d9c07001250059ded430648469e2'
client = Client(account_sid, auth_token)

client.messages.create(
                     body="https://www.figma.com/proto/dosS0tkqBeAAKR0OUs4Zht/SOURDOE?node-id=3%3A142&scaling=scale-down&page-id=0%3A1&starting-point-node-id=2%3A2",
                     from_= '+19592144471',
                     to= '+16049708617'
                 )

