import logging
from datetime import datetime

import driver
from GLOBALS import IKON_LOGIN_URL, IKON_LOGIN_USERNAME, IKON_LOGIN_PASSWORD

# Set the global format for logging messages
global_formatter = '%(asctime)s-%(levelname)s-%(message)s'
# Write logs to a file in './logs'
logging.basicConfig(filename=f'./logs/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log',
                    format= global_formatter,
                    level=logging.INFO)

# Also output logs to the console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console_formatter = logging.Formatter(global_formatter)
console.setFormatter(console_formatter)
logging.getLogger().addHandler(console)

mountain = 'Crystal Mountain Resort'  # TODO: Update to be dynamic
reservation_date = 'Dec 25 2020'  # TODO: Update to be dynamic

logging.info(
    f'Attempting to make a reservation at "{mountain}" on "{reservation_date}" for user "{IKON_LOGIN_USERNAME}".')

# Instantiate the driver.
reservation_driver = driver.Driver(IKON_LOGIN_URL, IKON_LOGIN_USERNAME, IKON_LOGIN_PASSWORD, reservation_date)

# Login into the Ikon reservation portal.
reservation_driver.login()

# Navigate to the reservation page.
reservation_driver.navigate(identifier='sc-AxjAm ')

reservation_driver.check_availability()





