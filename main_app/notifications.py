# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf3e003bdb5344e1d9915b07ab6902841'
auth_token = '6c8bd6658904a7dbc1bf35edeac611e5'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Congrats you can code!!!!!!',
                              from_='+12018244246',
                              to='+12105288184'
                          )

print(message.sid)