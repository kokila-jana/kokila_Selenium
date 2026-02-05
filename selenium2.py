'''XPATH'''
# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# # from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.google.com/")
# t.sleep(5)
# a.find_element(By.XPATH,'/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[3]/textarea').send_keys("dhoni")
# t.sleep(5)

'''CSS SELECTOR'''
# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# # from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.google.com/")
# t.sleep(5)
# a.find_element(By.CSS_SELECTOR,'.gLFyf').send_keys("dhoni")
# t.sleep(5)

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# # from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://practice.expandtesting.com/radio-buttons")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="red"]').click()
# t.sleep(10)
# a.find_element(By.XPATH,'//*[@id="yellow"]').click()
# t.sleep(5)


# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# # from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://total-qa.com/checkbox-example/")
# a.find_element(By.XPATH,'//*[@id="post-3261"]/div/p/input[1]').click()
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="post-3261"]/div/p/input[1]').click()
# t.sleep(5)

import selenium
from  selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import time as t
a=webdriver.Chrome()
a.maximize_window()
a.get("https://demoqa.com/text-box")
a.find_element(By.XPATH,'//*[@id="userName"]').send_keys("kokila"+Keys.TAB)
t.sleep(5)
a.find_element(By.XPATH,'//*[@id="userEmail"]').send_keys("kokilagur@gmail.com"+Keys.TAB)
t.sleep(5)
a.find_element(By.XPATH,'//*[@id="currentAddress"]').send_keys("Salem"+Keys.TAB)
t.sleep(5)
a.find_element(By.XPATH,'//*[@id="permanentAddress"]').send_keys("Namakkal")
t.sleep(5)
a.find_element(By.XPATH,'//*[@id="submit"]').click()
t.sleep(5)


