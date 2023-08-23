import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.voki.com/site/create")
wait = WebDriverWait(driver, 20)

# Updated locator for the music icon
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@title='Voice']")))
element.click()

# Wait for the text box to be clickable, click it, and enter text
text_box = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ve-voice-text"]')))
text_box.click()
text_box.clear()
text_box.send_keys("Hello, How are you? Are you available tomorrow? let's get some fun")

# wait until the play button is clickable
play_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ve-control-bar9"]/div[2]/div[5]/div[1]/img[1]')))
play_button.click()  # click the play button

# Add a delay at the end to allow the audio to play
time.sleep(10)