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

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demoqa.com/text-box")
# a.find_element(By.XPATH,'//*[@id="userName"]').send_keys("kokila"+Keys.TAB)
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="userEmail"]').send_keys("kokilagur@gmail.com"+Keys.TAB)
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="currentAddress"]').send_keys("Salem"+Keys.TAB)
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="permanentAddress"]').send_keys("Namakkal")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="submit"]').click()
# t.sleep(5)


# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demoqa.com/text-box")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="userName"]').send_keys("kokila")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="userName"]').clear()
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="userName"]').send_keys("Jana")
# t.sleep(5)

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demoqa.com/text-box")
# t.sleep(5)
# b=a.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/h1').text
# print(b)

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demoqa.com/text-box")
# b=a.find_element(By.XPATH,'//*[@id="userName"]')
# print(b.get_attribute("autocomplete"))
# print(b.get_attribute("placeholder"))
# print(b.get_attribute("class"))
# print(b.get_attribute("id"))
# print(b.get_attribute("type"))

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demoqa.com/text-box")
# b=a.find_element(By.XPATH,'//*[@id="userName"]')
# print(b.value_of_css_property("width"))
# print(b.value_of_css_property("height"))
# print(b.value_of_css_property("color"))
# print(b.value_of_css_property("font-size"))
# print(b.value_of_css_property("font-family"))

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.mxplayer.in/")
# b=a.find_element(By.LINK_TEXT,'Movies')
# print(b.is_displayed())

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://practice.expandtesting.com/radio-buttons")
# b=a.find_element(By.XPATH, '//*[@id="red"]')
# print(b.location)

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# from PIL import Image
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.mxplayer.in/")
# t.sleep(5)
# a.save_screenshot("D:\\kokila ppts\\my selinum\\img.PNG")
# b=Image.open("D:\\kokila ppts\\my selinum\\img.PNG")
# b.show()

# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.get("https://www.amazon.in/")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("Phone"+Keys.ENTER)
# t.sleep(5)
# a.back()
# t.sleep(5)
# a.forward()
# t.sleep(5)
# a.refresh()
# t.sleep(5)

'''1.To scroll down the web page by pixel'''
# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# t.sleep(5)
# a.execute_script("window.scrollBy(11874,1067)")
# t.sleep(10)

'''2.To scroll down the web page by the visibility of the element'''
# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# t.sleep(5)
# b=a.find_element(By.XPATH,'/html/body/div[4]/section/div/div/div[3]/div/div/a[9]/div/img')
# a.execute_script("arguments[0].scrollIntoView()",b)
# t.sleep(5)

'''To scroll down/up of the web page at the bottom/top of the page'''
# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# t.sleep(5)
# a.execute_script("window.scrollTo(0,document.body.scrollHeight)")#bottom
# t.sleep(5)
# a.execute_script("window.scrollTo(0,-document.body.scrollHeight)")#top
# t.sleep(5)

'''Horizontal scroll on the web page'''
# import selenium
# from  selenium import webdriver
# from selenium.webdriver.common.by import By
# from  selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.alton.co.in/")
# t.sleep(5)
# a.execute_script('window.scrollBy(1504,0)')
# t.sleep(5)


'''Actionchins'''
'''click()'''
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
#
# a = webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# b=a.find_element(By.LINK_TEXT,'JavaScript')
# action=ActionChains(a)
# action.click(on_element=b)
# t.sleep(5)
# action.perform()

'''click_and_hold'''
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
#
# a = webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# b=a.find_element(By.LINK_TEXT,'Compilers')
# action=ActionChains(a)
# action.click_and_hold(on_element=b)
# t.sleep(5)
# action.perform()
# t.sleep(5)


'''double_click and right_click'''
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
#
# a = webdriver.Chrome()
# a.maximize_window()
# a.get("https://artoftesting.com/samplesiteforselenium")
# b=a.find_element(By.XPATH,'//*[@id="dblClkBtn"]')
# action=ActionChains(a)
# action.double_click(on_element=b)
# # action.context_click(on_element=b)
# t.sleep(5)
# action.perform()
# t.sleep(5)


# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
#
# a = webdriver.Chrome()
# a.maximize_window()
# a.get('https://artoftesting.com/samplesiteforselenium')
# source=a.find_element(By.XPATH,'//*[@id="myImage"]')
# dest=a.find_element(By.XPATH,'//*[@id="targetDiv"]')
# action=ActionChains(a)
# action.drag_and_drop(source,dest).perform()
# t.sleep(5)


# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
#
# a = webdriver.Chrome()
# a.maximize_window()
# a.get("https://vinothqaacademy.com/multiple-windows/")
# a.find_element(By.NAME,'145newbrowsertab234').click()
# t.sleep(5)
# child=a.window_handles[1]
# a.switch_to.window(child)
# t.sleep(5)
# a.find_element(By.LINK_TEXT,'Home').click()
# t.sleep(5)
# parent=a.window_handles[0]
# a.switch_to.window(parent)
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="button1"]').click()
# t.sleep(5)

# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t

# a = webdriver.Chrome()
# a.maximize_window()
# a.get("https://vinothqaacademy.com/multiple-windows/")
# a.find_element(By.NAME,'newbrowserwindow123').click()
# t.sleep(5)
# child=a.window_handles[1]
# a.switch_to.window(child)
# # t.sleep(5)
# b=a.find_element(By.XPATH,'//*[@id="addBtn"]').text
# print(b)


# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.google.com/")
# a.find_element(By.XPATH,'//*[@id="APjFqb"]').click()
# t.sleep(5)
# action=ActionChains(a)
# action.key_up(Keys.SHIFT).send_keys("dhoni")
# action.perform()
# t.sleep(5)

# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.facebook.com/")
#
# wait = WebDriverWait(a, 10)
# element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#email')))
# element.send_keys("kokila")
# e2=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="pass"]')))
# e2.send_keys("jana12345")


# a=[]
# n=5
# for i in range(1,n+1):
#     b=int(input("enter"))
#     a.append(b)
# print(a)


# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tutorialspoint.com/selenium/practice/text-box.php")
# a.find_element(By.XPATH,'//*[@id="fullname"]').send_keys("kokila")
# t.sleep(5)
# action=ActionChains(a)
# action.key_down(Keys.CONTROL).send_keys("a").perform()
# t.sleep(5)
# # action.key_down(Keys.CONTROL).send_keys("c").perform()
# action.key_down(Keys.CONTROL).send_keys("x").perform()
# a.find_element(By.XPATH,'//*[@id="email"]').click()
# t.sleep(5)
# action.key_down(Keys.CONTROL).send_keys("v").perform()
# t.sleep(5)

# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# action=ActionChains(a)
# b=a.find_element(By.XPATH,'/html/body/div[4]/section/div/div/div[4]/div/div/a[12]/div/img')
# action.move_to_element(b).perform()
# t.sleep(5)

# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
# b=a.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
# action=ActionChains(a)
# action.click_and_hold(b).move_by_offset(19,20).perform()
# t.sleep(6)


# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://practice.expandtesting.com/upload")
# a.find_element(By.XPATH,'//*[@id="fileInput"]').send_keys("C:\\Users\\manojana\\Downloads\\mini_project.docx")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="fileSubmit"]').click()
# t.sleep(5)

# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import time as t
# try:
#     a=webdriver.Chrome()
#     a.maximize_window()
#     a.get("https://sample-files.com/documents/pdf/")
#     a.find_element(By.XPATH,'//*[@id="post-106"]/div/div/p[]/a').click()
#     t.sleep(5)
# except Exception as e:
#     print(e)
# print("vjnjvn")


# try:
#     a=int(input("enter"))
#     b=int(input("enter"))
#     c=a+b
#     print(c)
# except Exception as e:
#     print(e)
# finally:
#     print("hello")

# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://practice.expandtesting.com/tooltips")
# b=a.find_element(By.XPATH,'//*[@id="btn1"]')
# print(b.get_attribute("title"))


# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# x="What's new in 3.2"
# a.get("https://demo.guru99.com/test/tooltip.html")
# b=a.find_element(By.XPATH,'//*[@id="download_now"]')
# action=ActionChains(a)
# action.click_and_hold().move_to_element(b).perform()
# b=a.find_element(By.XPATH,'//*[@id="demo_content"]/div/div/div/a').text
# print(b)
# assert x==b
# print("test case pass")
#
#
# # if x==b:
# #     print("testcase pass")
# # else:
# #     print("testcase failed...")
# t.sleep(5)


# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import time as t
#
# a = webdriver.Chrome()
# a.maximize_window()
# a.get("https://practice.expandtesting.com/tables")
# row = a.find_elements(By.XPATH, '//*[@id="table1"]/tbody/tr')
# print(len(row))
# column = a.find_elements(By.XPATH, '//*[@id="table1"]/thead/tr/th')
# print(len(column))
# header = a.find_element(By.XPATH, '//*[@id="table1"]/thead/tr')
# print(header.text)
# row_value=a.find_element(By.XPATH,'//*[@id="table1"]/tbody/tr[4]')
# print(row_value.text)
# col_value=a.find_element(By.XPATH,'//*[@id="table1"]/tbody/tr/td[3]')
# print(col_value.text)

#
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# import time as t
#
# a = webdriver.Chrome()
# a.maximize_window()
# a.get("https://demo.automationtesting.in/Alerts.html")
'''simple alert'''
# a.find_element(By.XPATH,'//*[@id="OKTab"]/button').click()
# t.sleep(5)
# a.switch_to.alert.accept()
# t.sleep(5)

'''ok or cancel'''
# a.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="CancelTab"]/button').click()
# t.sleep(3)
# # a.switch_to.alert.accept()
# a.switch_to.alert.dismiss()
# t.sleep(5)

# a.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="Textbox"]/button').click()
# b=a.switch_to.alert
# print(b.text)
# b.send_keys("Kokila")
# t.sleep(3)
# b.accept()
# t.sleep(5)



# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time as t
# a=webdriver.Chrome()
# a.get("https://practice.expandtesting.com/tables")
# t.sleep(5)
# tables = a.find_elements(By.TAG_NAME, "table")
#
# for table in tables:
#     rows = table.find_elements(By.TAG_NAME, "tr")
#     for row in rows:
#         cells = row.find_elements(By.TAG_NAME, "td")
#         print([cell.text for cell in cells])

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
import requests
a=webdriver.Chrome()
a.get("https://demo.guru99.com/test/newtours/")
image=a.find_elements(By.TAG_NAME,'img')
for i in image:
    src=i.get_attribute("src")
    result=requests.head(src)
    if result.status_code==200:
        print(src,result.status_code)






