from Pageactions.commonfunctions import CommonFunctions
from Pageobjects.Facbook_objectlocaters import FacebookLogin
import time
import yaml


with open('../Testdata/f_cratecreds.yaml', 'r') as file:
    f_cratecreds = yaml.full_load(file)

cfuntion = CommonFunctions()
g_objects = FacebookLogin()

cfuntion.open_url('https://en-gb.facebook.com/')
time.sleep(2)
cfuntion.maximize()
time.sleep(2)
cfuntion.click_on_elements(g_objects.createnew_xpath)
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.firstname_xpath, f_cratecreds['firstname'])
cfuntion.click_on_inputs_send_keys(g_objects.surename_xpath, f_cratecreds['surname'])
cfuntion.click_on_inputs_send_keys(g_objects.mobileno_xpath, f_cratecreds['mobileno'])
cfuntion.click_on_inputs_send_keys(g_objects.newpassword_xpath, f_cratecreds['password'])
cfuntion.click_on_inputs_send_keys(g_objects.day_xpath, f_cratecreds['date'])
cfuntion.click_on_inputs_send_keys(g_objects.mounth_xpath, f_cratecreds['month'])
cfuntion.click_on_inputs_send_keys(g_objects.year_xpath, f_cratecreds['year'])
cfuntion.click_on_elements(g_objects.gender_xpath)
cfuntion.click_on_elements(g_objects.sigin_xpath)
