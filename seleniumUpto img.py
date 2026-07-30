# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.firstcry.com/")
# a.find_element(By.LINK_TEXT,' Toys').click()
# t.sleep(5)

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

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.amazon.in/")
# t.sleep(5)
# # a.find_element(By.ID,'twotabsearchtextbox').send_keys("Phone")
# a.find_element(By.CLASS_NAME,'nav-input nav-progressive-attribute').send_keys("Phone")
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.google.com/")
# t.sleep(5)
# a.find_element(By.CLASS_NAME,'gLFyf').send_keys("Phone")
# a.find_element(By.TAG_NAME,'textarea').send_keys('Dhoni')
# a.find_element(By.NAME,'q').send_keys("kokila")
# a.find_element(By.LINK_TEXT,'Gmail').click()
# # a.find_element(By.PARTIAL_LINK_TEXT,'Gma').click()
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# t.sleep(5)
# a.find_element(By.PARTIAL_LINK_TEXT,'JavaS').click()
# # a.find_element(By.LINK_TEXT,'JavaScript').click()
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://opensource-demo.orangehrmlive.com/")
# t.sleep(5)
# a.find_element(By.CSS_SELECTOR,'#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div > div:nth-child(2) > input').send_keys("kokila")
# a.find_element(By.CSS_SELECTOR,'input[name="username"]').send_keys("Admin")
# a.find_element(By.CSS_SELECTOR,'.oxd-input oxd-input--active').send_keys("Admin")
# a.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("kokila")
# a.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("kokila")
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://testautomationpractice.blogspot.com/")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="sunday"]').click()
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="monday"]').click()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="tuesday"]').click()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="male"]').click()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="female"]').click()
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://testautomationpractice.blogspot.com/")
# t.sleep(5)
# a.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-input"]').send_keys("kokila"+Keys.ENTER)
# t.sleep(5)


# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.amazon.in/")
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("Phone"+Keys.ENTER)
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').clear()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("Laptop"+Keys.ENTER)
# t.sleep(3)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://testautomationpractice.blogspot.com/")
# t.sleep(3)
# # b=a.find_element(By.XPATH,'//*[@id="HTML15"]/h2').text
# b=a.find_element(By.XPATH,'//*[@id="name"]')
# print(b.value_of_css_property("height"))
# print(b.value_of_css_property("width"))
# print(b.value_of_css_property("font-size"))
# print(b.value_of_css_property("background-color"))
# print(b.value_of_css_property("border"))


# print(b.get_attribute("class"))
# print(b.get_attribute("id"))
# print(b.get_attribute("maxlength"))
# print(b.get_attribute("placeholder"))
# print(b.get_attribute('type'))

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://in.bookmyshow.com/explore/home/")
# t.sleep(3)
# b=a.find_element(By.XPATH,'//*[@id="super-container"]/div/div[1]/div[2]/div/div/div[1]/div/a[2]').is_displayed()
# print(b)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# from PIL import Image
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://practice.expandtesting.com/radio-buttons")
# t.sleep(3)
# a.save_screenshot("C:\\Users\\manojana\\OneDrive\\Desktop\\kk.png")
# x=Image.open("C:\\Users\\manojana\\OneDrive\\Desktop\\kk.png")
# x.show()

# b=a.find_element(By.XPATH,'//*[@id="core"]/div/div/div[2]/div[2]/div/div[2]').location
# print(b)
# b=a.find_element(By.XPATH,'//*[@id="red"]')
# t.sleep(5)
# b.click()
# print(b.is_selected())


# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.amazon.in/")
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("Laptop"+Keys.ENTER)
# t.sleep(5)
# a.back()
# t.sleep(2)
# a.forward()
# t.sleep(2)
# a.refresh()
# t.sleep(2)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://testautomationpractice.blogspot.com/")
# t.sleep(3)
# a.execute_script("window.scrollBy(990,700)")
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# t.sleep(3)
# b=a.find_element(By.XPATH,'/html/body/div[4]/section/div/div/div[4]/div/div/a[2]/div/div')
# a.execute_script("arguments[0].scrollIntoView()",b)
# t.sleep(7)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# t.sleep(3)
# a.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# t.sleep(7)
# a.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
# t.sleep(5)

#
# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.alton.co.in/")
# t.sleep(3)
# a.execute_script("window.scrollBy(1504,0)")
# t.sleep(5)


# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.tpointtech.com/")
# t.sleep(3)
# b=a.find_element(By.XPATH,'//*[@id="navbarCollapse"]/div/div[1]/a')
# action=ActionChains(a)
# action.click_and_hold(on_element=b)
# action.perform()
# t.sleep(5)
# b=a.find_element(By.XPATH,'/html/body/div[4]/section/div/div/div[1]/div/div/a[1]/div')
# action=ActionChains(a)
# action.click(on_element=b)
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
# b=a.find_element(By.XPATH,'//*[@id="dblClkBtn"]')
# action=ActionChains(a)
# action.double_click(on_element=b)
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
# a.switch_to.alert.accept()
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

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demo.automationtesting.in/Alerts.html")
# t.sleep(3)

# from selenium import webdriver
# import time as t
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# # Create ChromeOptions object
# options = webdriver.ChromeOptions()
#
# # Add options
# options.add_argument("--start-maximized")
# options.add_argument("--incognito")
# options.add_argument("--disable-notifications")
#
# # Pass options when creating the driver
# driver = webdriver.Chrome(options=options)
#
# driver.get("https://www.firstcry.com/")
# t.sleep(5)
#
# print(driver.title)
# driver.find_element(By.XPATH,'//*[@id="search_box"]').send_keys("toys"+Keys.ENTER)
# t.sleep(5)
# driver.quit()

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demo.automationtesting.in/Windows.html")
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()
# t.sleep(5)
# c=a.window_handles[1]
# a.switch_to.window(c)
# a.find_element(By.XPATH,'//*[@id="main_navbar"]/ul/li[3]/a/span').click()
# t.sleep(5)
# p=a.window_handles[0]
# a.switch_to.window(p)
# t.sleep(5)
# a.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.google.com/")
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="APjFqb"]')
# action=ActionChains(a)
# # action.key_down(Keys.SHIFT).send_keys("laptop").perform()
# action.key_up(Keys.SHIFT).send_keys("laptop").perform()
# t.sleep(5)
# print("ok")



# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://automationintesting.com/selenium/testpage/")
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="firstname"]').send_keys("Kokila")
# t.sleep(3)
# action=ActionChains(a)
# action.key_down(Keys.CONTROL).send_keys('a').perform()
# t.sleep(3)
# action.key_down(Keys.CONTROL).send_keys('c').perform()
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="surname"]').click()
# t.sleep(2)
# action.key_down(Keys.CONTROL).send_keys('v').perform()
# t.sleep(3)


# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demo.automationtesting.in/Register.html")
# t.sleep(3)
# a.find_element(By.XPATH,'//*[@id="imagesrc"]').send_keys("D:\\kokila ppts\\my selinum\\selenium notes.docx")
# t.sleep(5)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demo.automationtesting.in/FileDownload.html")
# t.sleep(3)
# a.find_element(By.XPATH,'/html/body/section/div[1]/div/div/div[1]/a').click()
# t.sleep(5)


# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://www.educative.io/")
# t.sleep(3)
# b=a.find_element(By.XPATH,'//*[@id="educative-branding-logo"]')
# print(b.get_attribute("title"))


# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://demo.guru99.com/test/tooltip.html")
# t.sleep(3)
# b=a.find_element(By.XPATH,'//*[@id="download_now"]')
# action=ActionChains(a)
# action.click_and_hold(on_element=b).perform()
# c=a.find_element(By.XPATH,'//*[@id="demo_content"]/div/div/div/a')
# print(c.text)

# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time as t
# a=webdriver.Chrome()
# a.maximize_window()
# a.get("https://practice.expandtesting.com/tables")
# t.sleep(3)
# b=a.find_elements(By.XPATH,'//*[@id="table1"]/tbody/tr')
# print(len(b))
# c=a.find_elements(By.XPATH,'//*[@id="table1"]/thead/tr/th')
# print(len(c))
# d=a.find_element(By.XPATH,'//*[@id="table1"]/thead/tr')
# print(d.text)
# e=a.find_element(By.XPATH,'//*[@id="table1"]/tbody/tr[1]')
# print(e.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as r
a=webdriver.Chrome()
a.get("https://demo.guru99.com/test/newtours/")
a.maximize_window()
link=a.find_elements(By.TAG_NAME,"img")
for i in link:
    att=i.get_attribute("src")
    res=r.head(att)
    if res.status_code!=200:
        print(att)

