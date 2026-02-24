from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time


chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

driver = webdriver.Chrome(chrome_options)

driver.get("file:///D:/kokila ppts/Web designing/DICTIONARY-APP/DICTIONARY-APP/dictionary.html")

driver.maximize_window()

driver.find_element(By.ID, "myword").click()
time.sleep(2)

search_box = driver.find_element(By.ID, "myword")
search_box.send_keys("life")

driver.find_element(By.ID, "search-btn").click()
time.sleep(3)

language = Select(driver.find_element(By.ID, "language-select"))

languages = ["hi", "ml", "te", "fr"]

for lang in languages:
    language.select_by_value(lang)
    driver.find_element(By.ID, "search-btn").click()
    time.sleep(3)

try:
    voice_btn = driver.find_element(By.ID, "voice-btn")
    voice_btn.click()
    print("Voice button clicked successfully")
    time.sleep(5)
except:
    print("Voice button not working")

try:
    pronounce_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Pronounce')]")
    pronounce_btn.click()
    print("Pronounce button clicked")
    time.sleep(2)
except:
    print("Pronounce button not found")

pages = ["Introduction", "Technologies Used", "Advantages", "App"]

for page in pages:
    driver.find_element(By.LINK_TEXT, page).click()
    time.sleep(2)


screenshot_path = "D:\\kokila ppts\\Web designing\\DICTIONARY-APP\\dictionary_test.png"
driver.save_screenshot(screenshot_path)

print("Screenshot saved at:", screenshot_path)

img = Image.open(screenshot_path)
img.show()


driver.quit()
