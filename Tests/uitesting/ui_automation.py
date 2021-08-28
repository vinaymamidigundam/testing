"""
    this file is used for user interface of application
"""
from PageActions.commonfunctions import Automation_texting
from PageObjects.automation_obj import Automation
import time
import yaml

with open('../Testdata/create.yaml', 'r') as file:
    create = yaml.full_load(file)

cfuntion = Automation_texting()
g_objects = Automation

cfuntion.open_url('https://testautomationpractice.blogspot.com/?m=1')
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.searchinput_xpath, create['search_input'])
cfuntion.click_on_elements(g_objects.searchbutton)
cfuntion.click_on_elements(g_objects.clcik)
cfuntion.arlts()
cfuntion.click_on_elements(g_objects.datepicker)
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.select_a_speed, create['speed'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.select_a_fils, create['fil'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.select_a_number, create['number'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.select_a_products, create['product'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.select_a_animals, create['animal'])
time.sleep(2)
cfuntion.switch_to_frame(g_objects.main_section)
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.first_name, create['firstname'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.last_name, create['lastname'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.phone_number, create['mobileno'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.country, create['Country'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.city, create['city'])
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.email_enter, create['Email Address'])
time.sleep(2)
cfuntion.click_on_elements(g_objects.gender)
time.sleep(2)
cfuntion.click_on_elements(g_objects.best_day)
time.sleep(2)
cfuntion.click_on_elements(g_objects.best_time)
time.sleep(2)
# function.switch_to_frame(g_objects.rightsize_xpath)
