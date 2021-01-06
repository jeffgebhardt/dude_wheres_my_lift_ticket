import time
import sys

from driver import driver
from logger import logger
from messenger import messenger

from GLOBALS import IKON_LOGIN_URL, \
    IKON_LOGIN_USERNAME, \
    IKON_LOGIN_PASSWORD, \
    RESERVATION_ATTEMPT_RETRY_INTERVAL_SECONDS, \
    TWILIO_TO_NUMBER

mountain = 'crystal_mountain_resort'  # TODO: Make dynamic

if len(sys.argv) != 2:
    logger.info('Please supply a reservation date.')
    exit()

reservation_date = sys.argv[1]

logger.info(f'Attempting to make a reservation at "{mountain}" on "{reservation_date}" for user '
            f'"{IKON_LOGIN_USERNAME}".')

# Instantiate the driver.
reservation_driver = driver.Driver(IKON_LOGIN_URL, IKON_LOGIN_USERNAME, IKON_LOGIN_PASSWORD, reservation_date)

try:
    # Login into the Ikon reservation portal.
    logger.info(f'Logging into "{IKON_LOGIN_URL}" with username "{IKON_LOGIN_USERNAME}" and password '
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
            # Send SMS to user
            messenger = messenger.Messenger()
            message_body = f'Hello from "Dude wheres my lift ticket". We found an available reservation on ' \
                           f'{reservation_date} and reserved it. Shred on!'
            messenger.send_sms(TWILIO_TO_NUMBER, message_body)
            logger.info(f'Successfully reserved day at {mountain} for {reservation_date} and informed user.')
            exit()

        # Wait designated retry interval and then refresh page before trying again
        time.sleep(RESERVATION_ATTEMPT_RETRY_INTERVAL_SECONDS)
        reservation_driver.navigate(direction='refresh')
finally:
    reservation_driver.close_driver()
