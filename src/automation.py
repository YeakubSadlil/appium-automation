from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.common.exceptions import NoSuchElementException
import time

capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'deviceId',        # deviceid will be your device id by the command 'adb devices'
    # 'platformVersion': '12.0',     # Optional - Remove this if you want to run on any Android version
    'appPackage': 'com.bKash.customerapp',
    'appActivity': 'com.bKash.customerapp.MainActivity',
    'noReset': True,
    'fullReset': False,
    'autoGrantPermissions': True
}

your_pin = 'Your_PIN'   # replace with your bKash PIN
appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

driver.implicitly_wait(5)

# Handle location popup
try:
    no_thanks_button = driver.find_element(By.ID, 'android:id/button2')
    no_thanks_button.click()
    print("Clicked on 'No thanks'")
except NoSuchElementException:
    print("'No thanks' button not found")

time.sleep(1)

try:
    pin_input_field = driver.find_element(
        By.ANDROID_UIAUTOMATOR, 
        'new UiSelector().description("| Enter bKash PIN")'
    ).click()
        
    print("Found PIN input field")

    # Send the PIN
    if pin_input_field:
        pin_input_field.send_keys(your_pin)
        print("PIN Typed")
    
except NoSuchElementException:
    print("PIN input field not found")

time.sleep(3)

try:
    next_button = driver.find_element(By.ACCESSIBILITY_ID, "Next").click()
    print("Clicked Next button")

except NoSuchElementException:
    print("Next button not found")

time.sleep(3)

try:
    balance_button = driver.find_element(By.ACCESSIBILITY_ID, "Tap for Balance").click()
    print("Clicked Balance button")
    
except NoSuchElementException:
    print("Balance button not found")


# driver.quit()
