from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Automation_texting:
    """
            this class will do      -
                all the below the actions| functions

    """

    def __init__(self):
        self.browser = webdriver.Chrome("/home/vinay/selenium/chromedriver")

    def open_url(self, url):
        """
            this function will do   -
                - open the url
        :param url:
        :return:get_url
        """
        self.browser.get(url)

    def maximize(self):
        """
            this function will do   -
                - maximize the window
        :return:maximize_window
        """
        self.browser.maximize_window()

    def getpage_title(self):
        """
            this function will do   -
                - get the page title
        :return:page title
        """
        return self.browser.title

    def click_on_inputs_send_keys(self, x_path, value):
        """
            this function will do   -
               -root the x_path and enter the value
        :param x_path:element x_path
        :param value:input value
        :return:x_path,value
        """
        self.browser.find_element_by_xpath(x_path).send_keys(value)

    def click_on_elements(self, x_path):
        """
            this function will do   -
                -root the x_path and click itself
        :param x_path:
        :return:
        """
        time.sleep(2)
        self.browser.find_element(By.XPATH, x_path).click()

    def select_on_element(self, x_path):
        """
            this function will do   -
                - root the x_path
        :param x_path:
        :return:
        """
        self.browser.find_element(By.XPATH, x_path)

    def arlts(self):
        """
            this function will to  -
                - alert handling
        :return:alert hading
        """
        self.browser.switch_to.alert.accept()

    def switch_to_frame(self, xpath):
        """
            This function will do -
                - switch the frame
        :return:
        """
        try:
            self.browser.switch_to.frame(self.browser.find_element_by_xpath(xpath))
        except NoSuchElementException:
            raise Exception("No element found")

    def double_click(self, xpath):
        """
            this function will do -
                -double_click on the botton
        :param xpath:
        :return:
        """
        action_chains = ActionChains(self.browser)
        action_chains.double_click(xpath).perform()

    def drag_and_drop(self, source, target):
        """
            this function will do  -
                -drag_and_drop
        :param source:
        :param target:
        :return:
        """
        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop(source, target).perform()

    def click_hold_move(self, source, target):
        """
            this function will do  -
                -hold and move the photo
        :param target:move the pic
        :param source:photo
        :param
        :return:pic moved one place to another place
        """

        action_chains = ActionChains(self.browser)
        action_chains.click_and_hold(source).move_to_element(target).release().perform()

    def slider_element(self, source, x_offset, y_offset):
        """
            this function will do   -
                - slider_element
        :param source:slider
        :param x_offset:0
        :param y_offset:10
        :return:slider is moved
        """
        acions_chains = ActionChains(self.browser)
        acions_chains.drag_and_drop_by_offset(source, x_offset, y_offset).perform()

    def scrollDown(self):
        """
            this function will do
                scrollDown
        :return:scrollDown
        """

        ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).perform()

    def scrollUp(self):
        """
            this function will do
                scrollUp
        :return: scrollUp
        """
        ActionChains(self.browser).send_keys(Keys.PAGE_UP).perform()

    def close(self):
        """
            this function will do   -
                - close the browser
        :return:close the browser
        """
        self.browser.close()

    def move_element(self, xpath, x_offset, y_offset):
        """
            this function will do   -
                move the slider
        :param xpath:to move slider
        :param x_offset:at starting point
        :param y_offset:at ending point
        :return:slider moved x to y
        """
        time.sleep(2)
        move_action = ActionChains(self.browser)
        move_action.click_and_hold(xpath).move_by_offset(x_offset, y_offset).release().perform()
