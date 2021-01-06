import os

# This shouldn't change... But if it does, we will probably figure it out after a few hours of debugging.
IKON_LOGIN_URL = 'https://account.ikonpass.com/en/login'

# Set your username and password as an environment variables in Powershell:
# $env:IKON_LOGIN_USERNAME = 'YOUR_USERNAME_HERE'
# $env:IKON_LOGIN_PASSWORD = 'YOUR_PASSWORD_HERE'
IKON_LOGIN_USERNAME = os.getenv('IKON_LOGIN_USERNAME')
IKON_LOGIN_PASSWORD = os.getenv('IKON_LOGIN_PASSWORD')

# This is the driver that is used for Selenium and headless web browsing. The driver version must match your installed
# version of Chrome.
CHROME_DRIVER_LOCATION = './chrome_driver/chromedriver.exe'

# How often in seconds to retry making a reservation
RESERVATION_ATTEMPT_RETRY_INTERVAL_SECONDS = 10

# Set the Twilio credentials as an environment variables in Powershell:
# $env:TWILIO_ACCOUNT_SID = 'SID_HERE'
# $env:TWILIO_AUTH_TOKEN = 'TOKEN_HERE'
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_FROM_NUMBER = '+12058986998'
# Set the to number as an environment variable in Powershell:
# $env:TWILIO_TO_NUMBER  = 'TO_NUMBER_HERE'
# Use the following format '=15556781111'
TWILIO_TO_NUMBER = os.environ['TWILIO_TO_NUMBER']

# If you have Crystal Mountain Resort selected as a favourite on the Ikon Pass site, leave this as true, otherwise
# set it to 'False'
CRYSTAL_STARRED = True
