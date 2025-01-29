from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('http://web.whatsapp.com')

name  = input('Enter the name of user or group: ')
msg = input('Enter the message: ')
count = int(input('Enter the count: '))

print(name, msg, count)

# Scan the QR code before proceeding further
input('Press ENTER after scanning QR code')

# Wait for the search box to appear and click it
search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
search_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, search_xpath)))
search_box.click()
search_box.send_keys(name + Keys.ENTER)

# Updated to use the title attribute within the span for selecting the conversation
conversation_title = name  # Assuming 'name' is the variable holding the conversation name you're searching for
conversation_xpath = f"//span[@title='{conversation_title}']"

# Wait for the conversation to be clickable after the search
conversation_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, conversation_xpath)))
conversation_element.click()

# After selecting the conversation
# Updated XPath to target the specific attributes of the message box
msg_box_xpath = '//div[@contenteditable="true" and @role="textbox" and @aria-label="Type a message"]'
msg_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, msg_box_xpath)))

for i in range(count):
    msg_box.send_keys(msg + Keys.ENTER)  # Send the message directly


# Scan the QR code before proceeding further
input('Press Enter')