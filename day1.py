from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t
a=webdriver.Chrome()
a.maximize_window()
a.get("https://www.firstcry.com/")
a.find_element(By.LINK_TEXT,' Toys').click()
t.sleep(5)

# a.get("https://opensource-demo.orangehrmlive.com/")
# t.sleep(5)
# a.find_element(By.NAME,'username').send_keys("kokila")
# t.sleep(5)


# a.get("https://www.google.com/")
# a.find_element(By.CLASS_NAME,'gLFyf').send_keys("Dhoni"+Keys.ENTER)
# t.sleep(5)

# a.get("https://www.facebook.com/")
# a.find_element(By.ID,'_R_1h6kqsqppb6amH1_').send_keys("Kokila")
# a.find_element(By.ID,'_R_1hmkqsqppb6amH1_').send_keys("jana123")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div').click()
# t.sleep(10)
