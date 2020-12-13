from twilio.rest import Client

from GLOBALS import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER


class Messenger:

    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.auth_token = TWILIO_AUTH_TOKEN
        self.from_number = TWILIO_FROM_NUMBER
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, to_number, message_body):
        message = self.client.messages.create(
                                        body=message_body,
                                        from_=self.from_number,
                                        to=to_number
        )

        return message.sid
