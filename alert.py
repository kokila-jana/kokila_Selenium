#from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://artoftesting.com/samplesiteforselenium")
# t.sleep(3)
# b=a.find_element(By.XPATH,'//*[@id="commonWebElements"]')
# action=ActionChains(a)
# action.context_click(on_element=b)
# action.perform()
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://artoftesting.com/samplesiteforselenium")
# t.sleep(3)
# s=a.find_element(By.XPATH,'//*[@id="myImage"]')
# d=a.find_element(By.XPATH,'//*[@id="targetDiv"]')
# ac=ActionChains(a)
# ac.drag_and_drop(s,d)
# ac.perform()
# t.sleep(5)


# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demo.automationtesting.in/Alerts.html")
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="OKTab"]/button').click()
# t.sleep(2)
# a.switch_to.alert.accept()
# t.sleep(3)
# a.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="CancelTab"]/button').click()
# t.sleep(3)
# # a.switch_to.alert.accept()
# a.switch_to.alert.dismiss()
# t.sleep(3)
# a.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="Textbox"]/button').click()
# b=a.switch_to.alert
# b.send_keys("kokila")
# b.accept()
# t.sleep(5)
# a.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="Textbox"]/button').click()
# b=a.switch_to.alert
# print(b.text)
