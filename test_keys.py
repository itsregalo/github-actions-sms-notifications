import africastalking
from decouple import config

AT_USERNAME = config('AT_USERNAME')
AT_API_KEY = config('AT_API_KEY')

africastalking.initialize(AT_USERNAME, AT_API_KEY)

sms = africastalking.SMS
response = sms.send(message="Workflows was successful", recipients=[f"{config('TO_PHONE_NUMBER')}"])