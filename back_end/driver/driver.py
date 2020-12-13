import time

from logger import logger
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from GLOBALS import CHROME_DRIVER_LOCATION, RESERVATION_ATTEMPT_RETRY_INTERVAL_SECONDS


class Driver:

    def __init__(self,
                 login_url,
                 username,
                 password,
                 reservation_date):
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
        self.wait = WebDriverWait(self.driver, 5)
        self.login_url = login_url
        self.previous_url = login_url
        self.username = username
        self.password = password
        self.reservation_date = reservation_date
        self.setup()

    def setup(self):
        self.driver.maximize_window()

    def get_login_form_info(self):
        self.driver.get(self.login_url)

        username_field_id = self.driver.find_element_by_id('email')
        password_field_id = self.driver.find_element_by_id('sign-in-password')
        submit_button_class = self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'submit')))

        return username_field_id, password_field_id, submit_button_class

    def login(self):

        username_field_id, password_field_id, submit_button_class = self.get_login_form_info()

        username_field_id.send_keys(self.username)
        password_field_id.send_keys(self.password)
        submit_button_class.click()

        self.validate_move()

    def navigate(self, *args, **kwargs):
        identifier = kwargs.get('identifier', None)
        direction = kwargs.get('direction', None)

        try:
            if len(kwargs.keys()) != 1:
                raise ValueError('Either an identifier or direction must be supplied to navigate().')
            if direction not in ('forwards', 'back', 'refresh', None):
                raise ValueError(f'Supplied direction: {direction}. Direction must be "forward", "back", '
                                 f'"refresh", or "None"')
        except ValueError as error:
            logger.error(error)
            exit()

        if identifier is not None:
            identifier_button = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, identifier)))
            identifier_button.click()
            self.validate_move()
        else:
            if direction == 'refresh':
                logger.info(f'Refreshing page "{self.driver.current_url}".')
                self.driver.refresh()
            if direction == 'forward':
                pass  # TODO: Implement
            if direction == 'back':
                pass  # TODO: Implement

    def check_availability(self):
        if self.driver.current_url != 'https://account.ikonpass.com/en/myaccount/add-reservations/':
            logger.info(f'Current URL must be "https://account.ikonpass.com/en/myaccount/add-reservations/" to proceed '
                        f'with making reservations, the current URL is "{self.driver.current_url}"')

        # This is the ID of the Crystal Mountain Resort element... TODO: Find a better way to do this.
        crystal_mountain_element = self.wait.until(
            ec.visibility_of_element_located((By.ID, 'react-autowhatever-resort-picker-section-3-item-0')))
        crystal_mountain_element.click()

        button = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'button.sc-AxjAm')))
        button.click()

        # TODO: Select proper month, right now we are assuming everything will be on the current month...
        self.driver.implicitly_wait(1)
        days_elements = self.driver.find_elements_by_class_name('DayPicker-Day')

        able_to_make_reservation = False

        for day in days_elements:
            day_value = day.get_attribute('aria-label')[4:]
            day_class = day.get_attribute('class')

            if 'unavailable' not in day_class and day_value == self.reservation_date:
                able_to_make_reservation = True
                logger.info(f'Reservation available for "{self.reservation_date}", attempting to reserve day.')
                day.click()

                # The day is now selected, we just need to save and complete the reservation.
                self.complete_reservation()
                self.driver.close()
                return True

        if not able_to_make_reservation:
            logger.info(f'Reservation NOT available for "{self.reservation_date}", will try again in '
                        f'{RESERVATION_ATTEMPT_RETRY_INTERVAL_SECONDS} seconds.')
            return False

    def complete_reservation(self):
        save_button = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.jxPclZ')))
        save_button.click()

        # Need to wait here for some reason...
        time.sleep(1)
        review_button = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                          'button.sc-AxjAm:nth-child(1)')))
        review_button.click()

        agree_checkbox = self.wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'input')))
        agree_checkbox.click()

        confirm_button = self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                                           'button.sc-AxjAm:nth-child(1)')))
        confirm_button.click()

    def validate_move(self):
        # We give the application 5 seconds to move to the new page before timing out
        timeout_count = 0

        while self.previous_url == self.driver.current_url:
            time.sleep(1)
            timeout_count += 1
            if timeout_count == 4:
                logger.info(f'Failed to navigate from {self.previous_url}.')
                exit()

        logger.info(f'Successfully navigated from {self.previous_url} to {self.driver.current_url}.')
        self.previous_url = self.driver.current_url

    def close_driver(self):
        logger.info('Closing the Chrome WebDriver.')
        self.driver.close()
