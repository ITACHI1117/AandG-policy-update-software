# Import the required modules
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from Write_logs import write_logs


# Main Function
def correct_reg_and_chassisNO(policy_number, reg_number, chassis_number,platform_data):
    # Provide the email and password
    email = platform_data[1]
    password = platform_data[2]

    # Provide policy number
    policy = policy_number
    correct_regNo = reg_number
    correct_chassisNo = chassis_number

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    # options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    path = (r"chromedriver.exe")
    service = Service(executable_path=path)
    driver = webdriver.Chrome(options=options, service=service)
    # driver.set_window_size(1920, 1080)

    # Send a get request to the url
    driver.get(platform_data[0])
    time.sleep(0.2)
    # https: // auth.geeksforgeeks.org /

    # Finds the input box by name in DOM tree to send both
    # the provided email and password in it.
    username = driver.find_element(by="xpath",
                                   value='//div[@class="col-md-offset-2 col-md-4 center-block panel-primary"]/input[1]')
    username.send_keys(email)
    keycode = driver.find_element(by="xpath",
                                  value='//div[@class="col-md-offset-2 col-md-4 center-block panel-primary"]/input[2]')
    keycode.send_keys(password)

    # Find the signin button and click on it.
    driver.find_element(by="xpath", value='//div/input[3]').click()
    time.sleep(0.2)

    # Find the Policy operations button and click on it.
    driver.find_element(
        by="xpath", value='//div[@class="menu-list"]/ul/ul/div[4]/div/li/a').click()
    time.sleep(0.2)

    # Find the Update Policy button and click on it.
    driver.find_element(
        by="xpath", value='//div[@class="menu-list"]/ul/ul/div[4]/div[2]/ul/li[2]').click()
    time.sleep(0.2)

    # Find the Search by option and click on it.
    driver.find_element(by="xpath",
                        value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div['
                              '3]/div/select').click()
    time.sleep(0.2)

    # Find the fetch by policy button and click on it.
    driver.find_element(by="xpath",
                        value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div['
                              '3]/div/select/option[2]').click()
    time.sleep(0.2)

    # Finds the input box by name in DOM tree to send
    # the provided Policy in it.
    policy_number = driver.find_element(by="xpath",
                                        value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary '
                                              'panel-heading"]/div/div[2]/input')
    policy_number.send_keys(policy)

    # Find the Fetch button and click on it.
    driver.find_element(by="xpath",
                        value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary '
                              'panel-heading"]/div/div[3]/input').click()
    time.sleep(1)
    # Checking if the screen is loading
    cssValue = driver.find_element(
        by="xpath", value='//div[4]').value_of_css_property('display')
    print(cssValue)
    # Waiting for Screen to load before Updating the policy
    while cssValue == 'block':
        cssValue = driver.find_element(
            by="xpath", value='//div[4]').value_of_css_property('display')
        print('Loading...')
        time.sleep(1.2)
        if cssValue == 'none':
            print("Done Loading✅")

    time.sleep(1)

    # checking for error message
    errobox_value = driver.find_element(
        by="xpath",
        value='//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable ui-resizable ui-dialog-buttons"][2]').value_of_css_property(
        'display')

    print(f"error value ={errobox_value}")
    ERROR_MESSAGE = ""
    if errobox_value == 'block':
        ERROR_MESSAGE = driver.find_element(
            by="xpath",
            value='//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable ui-resizable ui-dialog-buttons"][2]/div[2]').text
        print(f"error message ={ERROR_MESSAGE}  policy number = {policy}  regnumber = {reg_number}")
        return ERROR_MESSAGE,policy,chassis_number,correct_regNo
    else:
        print("policy found")

    time.sleep(0.2)

    # Checking the value of the reg
    valueofReg = driver.find_element(by="xpath",
                                     value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div['
                                           '8]/div[3]/input').get_attribute("value")
    if valueofReg == "":
        print("There was an error try again later")
        driver.close()
        driver.quit()
    else:
        print("no error")

    # Getting the value of the Reg Number So update on NIID can be made
    value_text = driver.find_element(by="xpath",
                                     value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div['
                                     '8]/div[3]/input')
    Reg_number = value_text.get_attribute("value")
    print(Reg_number)

    time.sleep(0.2)
    # Editing the Reg Number
    driver.find_element(by="xpath",
                        value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div['
                              '8]/div[3]/input').clear()
    reg_No = driver.find_element(by="xpath",
                                 value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary '
                                       'panel-heading"]/div[8]/div[3]/input')
    reg_No.send_keys(correct_regNo)

    time.sleep(0.2)

    #Getting the value of the chassis number
    value_text = driver.find_element(by="xpath",
                                     value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div[8]/div[2]/input')
    old_chassis_number = value_text.get_attribute("value")
    print(old_chassis_number)

    # Editing the Chassis Number
    driver.find_element(by="xpath",
                        value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div[8]/div[2]/input').clear()
    chassis_No = driver.find_element(by="xpath",
                                     value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div[8]/div[2]/input')
    chassis_No.send_keys(correct_chassisNo)

    time.sleep(0.2)

    # Find the Save button and click on it.
    driver.find_element(by="xpath",
                        value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div['
                              '14]/div/input').click()
    time.sleep(0.2)

    # Find the Yes button and click on it.
    driver.find_element(by="xpath",
                        value='//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable '
                              'ui-resizable ui-dialog-buttons"]/div/div/button').click()
    time.sleep(1)
    cssValue = driver.find_element(
        by="xpath", value='//div[4]').value_of_css_property('display')
    print(cssValue)
    # Waiting for Screen to load before Updating the policy
    while cssValue == 'block':
        cssValue = driver.find_element(
            by="xpath", value='//div[4]').value_of_css_property('display')
        print(cssValue)
        print('LOADING...')
        time.sleep(1.2)
        if cssValue == 'none':
            print("done waiting")

    # Geting the policy details
    POLICY_NUMBER = policy
    NEW_REGNUMBER = reg_number
    OLD_REGNUMBER = Reg_number
    NEW_CHASSIS_NUMBER = chassis_number
    OLD_CHASSIS_NUMBER = old_chassis_number

    # calling the write log function to write the log files
    write_logs(POLICY_NUMBER, NEW_REGNUMBER, OLD_REGNUMBER, NEW_CHASSIS_NUMBER, OLD_CHASSIS_NUMBER, None, None, "Reg_and_chassis_Update")
    print("Done✅")
    # Quits the driver
    driver.close()
    driver.quit()

    return Reg_number,policy,chassis_number,correct_regNo
