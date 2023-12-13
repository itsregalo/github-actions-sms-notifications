import africastalking
import os

AT_API_KEY = os.environ['AT_API_KEY']
AT_USERNAME = os.environ['AT_USERNAME']
AT_PHONE_NUMBER = os.environ['PHONE_NUMBER']

africastalking.initialize(AT_USERNAME, AT_API_KEY)

sms = africastalking.SMS
response = sms.send(message="Workflows was successful", recipients=[f"{AT_PHONE_NUMBER}"])