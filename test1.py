import time

from selenium.webdriver import Chrome
chromeDriver = 'C:\\temp\\chromedriver.exe'
driver = Chrome(chromeDriver)
driver.get('https://login.11st.co.kr/auth/front/login.tmall')
time.sleep(3)
input_login = driver.find_element_by_id("loginName")
input_login.send_keys("****")
input_pw = driver.find_element_by_id("passWord")
input_pw.send_keys("****")
btn = driver.find_element_by_class_name("btn_a")
time.sleep(3)
btn.click()
time.sleep(3)
driver.quit()