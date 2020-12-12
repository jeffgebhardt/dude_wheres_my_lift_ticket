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
