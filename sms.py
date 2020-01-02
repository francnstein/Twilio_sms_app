
# SMS PROGRAM USING TWILIO

from twilio.rest import Client
import acc

account_sid = acc.account_sid
auth_token = acc.auth_token
client = Client(account_sid, auth_token)
tel = acc.tel
twil = acc.twil

message = client.messages.create(
                    body='I look forward to sharing all the cool stuff we are working on',
                    to='+1'+tel,
                    from_= twil

                )

print(message.sid)


