import driver
from GLOBALS import IKON_LOGIN_URL, IKON_LOGIN_USERNAME, IKON_LOGIN_PASSWORD

mountain = 'Crystal Mountain Resort'  # TODO: Update to be dynamic
reservation_date = 'Dec 25 2020'  # TODO: Update to be dynamic

# Instantiate the driver.
reservation_driver = driver.Driver(IKON_LOGIN_URL, IKON_LOGIN_USERNAME, IKON_LOGIN_PASSWORD, reservation_date)

# Login into the Ikon reservation portal.
reservation_driver.login()

# Navigate to the reservation page.
reservation_driver.navigate(identifier='sc-AxjAm ')

reservation_driver.check_availability()





