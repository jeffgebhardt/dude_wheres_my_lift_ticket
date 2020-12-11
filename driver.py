import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from GLOBALS import CHROME_DRIVER_LOCATION


class Driver:

    def __init__(self,
                 login_url,
                 username,
                 password,
                 reservation_date):
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)

        # Stuff might break if you remove this, due to race conditions with selecting button elements...
        self.driver.implicitly_wait(3)
        self.login_url = login_url
        self.previous_url = login_url
        self.username = username
        self.password = password
        self.reservation_date = reservation_date
        self.username_field_id, self.password_field_id, self.submit_button_class = self.get_login_form_info()

        self.setup()

    def setup(self):
        self.driver.maximize_window()

    def get_login_form_info(self):
        self.driver.get(self.login_url)

        username_field_id = self.driver.find_element_by_id('email')
        password_field_id = self.driver.find_element_by_id('sign-in-password')
        submit_button_class = self.driver.find_element_by_class_name('submit')

        return username_field_id, password_field_id, submit_button_class

    def login(self):

        self.username_field_id.send_keys(self.username)
        self.password_field_id.send_keys(self.password)
        self.submit_button_class.click()

        # self.validate_move()

    def navigate(self, *args, **kwargs):
        identifier = kwargs.get('identifier', None)
        direction = kwargs.get('direction', None)

        try:
            if len(kwargs.keys()) != 1:
                raise ValueError('Either an identifier or direction must be supplied to navigate().')
            if direction not in ('forwards', 'back', 'refresh', None):
                raise ValueError(f'Supplied direction: {direction}. Direction must be "forwards", "back", '
                                 f'"refresh", or "None"')
        except ValueError as error:
            print(error)
            exit()

        if identifier is not None:
            time.sleep(2)
            button = self.driver.find_element_by_class_name(identifier)
            button.click()
            # self.validate_move()

            if self.driver.current_url == 'https://account.ikonpass.com/en/myaccount/add-reservations/':
                # This is us, selecting Crystal. TODO: Find a better way to do this.
                element = self.driver.find_element_by_id('react-autowhatever-resort-picker-section-3-item-0')
                element.click()
                time.sleep(2)

                button = self.driver.find_element_by_css_selector('button.sc-AxjAm')
                button.click()
                print('hello')
                # self.validate_move()
            else:
                # self.validate_move()
                pass
        else:
            # TODO: Implement direction
            pass

    def select_mountain(self, element):
        # Validate that we are on the correct page
        try:
            if self.driver.current_url != 'https://account.ikonpass.com/en/myaccount/add-reservations/':
                raise ValueError(f'The current URL must be "account.ikonpass.com/en/myaccount/add-reservations/" '
                                 f'to select a mountain.')
        except ValueError as error:
            print(error)
            exit()

        # TODO: Deselect all first

        select = Select(element)
        select.select_by_visible_text("Crystal Mountain Resort")

    def check_availability(self):
        # TODO: Select proper month, right now we are assuming everything will be on the current month...
        time.sleep(2)
        days_elements = self.driver.find_elements_by_class_name('DayPicker-Day')

        able_to_make_reservation = False

        for day in days_elements:
            day_value = day.get_attribute('aria-label')[4:]
            day_class = day.get_attribute('class')
            print(day_value)
            print(day_class)

            if 'unavailable' not in day_class and day_value == self.reservation_date:
                able_to_make_reservation = True
                print(f'Making reservation for {self.reservation_date}.')
                day.click()
                # Wait and then click save button. Use full class name!
                return

        if not able_to_make_reservation:
            print(f'{self.reservation_date} not available, will try again in x seconds.')
            # TODO: Retry logic


    def validate_move(self):
        timeout_count = 0

        while self.previous_url == self.driver.current_url:
            time.sleep(1)
            timeout_count += 1
            if timeout_count == 4:
                print(f'Failed to navigate from {self.previous_url}.')
                exit()

        print(f'Successfully navigated from {self.previous_url} to {self.driver.current_url}.')
        self.previous_url = self.driver.current_url


if __name__ == "__main__":
    test_url = 'https://account.ikonpass.com/'

    test_form_info = get_form_info(test_url)
