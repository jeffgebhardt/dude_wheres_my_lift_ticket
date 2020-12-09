import os

# This shouldn't change... But if it does, we will probably figure it out after a few hours of debugging.
LOGIN_URL = 'https://account.ikonpass.com/en/login'

# Set your username and password as an environment variables in Powershell:
# $env:IKON_LOGIN_USERNAME = 'YOUR_USERNAME_HERE'
# $env:IKON_LOGIN_PASSWORD = 'YOUR_PASSWORD_HERE'
LOGIN_USERNAME = os.getenv('IKON_LOGIN_USERNAME')
LOGIN_PASSWORD = os.getenv('IKON_LOGIN_PASSWORD')
