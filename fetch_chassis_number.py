# Import the required modules
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


from Write_logs import write_logs


# Main Function
def fetch_wrong_chassis(policy_number,chassis_number,platform_data,SHOW_WINDOW):
    # Provide the email and password
    email = platform_data[1]
    password = platform_data[2]

    # Provide policy number
    policy = policy_number
    correct_chassisNo = chassis_number

    options = webdriver.ChromeOptions()
    options.add_argument(SHOW_WINDOW)
    # options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    path = (r"chromedriver.exe")
    service = Service(executable_path=path)
    service.creation_flags = 0x08000000
    driver = webdriver.Chrome(options=options, service=service)
    driver.set_window_size(1200, 800)

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
        print(f"error message ={ERROR_MESSAGE}")
        return ERROR_MESSAGE,policy,correct_chassisNo
    else:
        print("policy found")


    # Checking the value of the reg
    valueofReg = driver.find_element(by="xpath",
                                     value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div['
                                           '8]/div[3]/input').get_attribute("value")
    if valueofReg == "":
        error_message = "There was an error try again later"
        driver.close()
        driver.quit()
        return error_message, policy, correct_chassisNo
    else:
        print("no error")

    # Getting the Reg Number So update on NIID can be made
    value_text = driver.find_element(by="xpath",
                                     value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div['
                                     '8]/div[3]/input')
    Reg_number = value_text.get_attribute("value")
    print(Reg_number)

    # Getting the value of the chassis number
    value_text = driver.find_element(by="xpath",
                                     value='//div[@class="col-md-offset-3 col-md-8 center-block panel-primary panel-heading"]/div[8]/div[2]/input')
    old_chassis_number = value_text.get_attribute("value")
    print(old_chassis_number)


    # calling the write log function to write the log files
    # write_logs(POLICY_NUMBER,None,None,NEW_CHASSIS_NUMBER,OLD_CHASSIS_NUMBER,None,None,"chassis_Update")
    print("Done✅")
    # Quits the driver
    driver.close()
    driver.quit()

    return Reg_number,policy,old_chassis_number
