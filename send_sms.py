import africastalking
import os
import sys

AT_API_KEY = os.environ['API_KEY']
AT_USERNAME = os.environ['USERNAME']
AT_PHONE_NUMBER = os.environ['PHONE_NUMBER']
MESSAGE = sys.argv[1]

africastalking.initialize(AT_USERNAME, AT_API_KEY)

sms = africastalking.SMS
response = sms.send(message=MESSAGE, 
                    recipients=[f"{AT_PHONE_NUMBER}"])