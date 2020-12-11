import time

import driver
from logger import logger
from GLOBALS import IKON_LOGIN_URL, IKON_LOGIN_USERNAME, IKON_LOGIN_PASSWORD, RESERVATION_ATTEMPT_RETRY_INTERVAL_SECONDS

mountain = 'Crystal Mountain Resort'  # TODO: Update to be dynamic
reservation_date = 'Dec 19 2020'  # TODO: Update to be dynamic

logger.info(f'Attempting to make a reservation at "{mountain}" on "{reservation_date}" for user '
            f'"{IKON_LOGIN_USERNAME}".')

# Instantiate the driver.
reservation_driver = driver.Driver(IKON_LOGIN_URL, IKON_LOGIN_USERNAME, IKON_LOGIN_PASSWORD, reservation_date)

# Login into the Ikon reservation portal.
logger.info(f'Attempting to log into "{IKON_LOGIN_URL}" with username "{IKON_LOGIN_USERNAME}" and password '
            f'"{IKON_LOGIN_PASSWORD.replace(IKON_LOGIN_PASSWORD, "*********")}"')
reservation_driver.login()

# Navigate to the add reservation page.
add_reservation_button_css_selector = 'a.sc-AxjAm:nth-child(2)'
reservation_driver.navigate(identifier=add_reservation_button_css_selector)

# Check availability loop
desired_date_reserved = False

while desired_date_reserved is False:
    desired_date_reserved = reservation_driver.check_availability()

    if desired_date_reserved:
        exit()

    # Wait designated retry interval and then refresh page before trying again
    time.sleep(RESERVATION_ATTEMPT_RETRY_INTERVAL_SECONDS)
    reservation_driver.navigate(direction='refresh')


