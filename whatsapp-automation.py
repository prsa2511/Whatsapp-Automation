from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException 
import time

def check_exists_by_xpath(xpath):
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException:
		print("no element")
		return False
	return True

contact = "Last benchers Ltians"
text = "Hey, this message was sent using Selenium"

#create cache and launch web whatsapp
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\prati\\Downloads")
#options.headless=True
driver=webdriver.Chrome(chrome_options=options)
actionChains=ActionChains(driver)
driver.get("https://web.whatsapp.com")
time.sleep(5)

#search chat
inp_xpath_search = "//div[@class='_2_1wd copyable-text selectable-text']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)

#locate archive button
#//span[@class='N2dUK']/span[@title='"+contact+"']/span[@class='matched-text _3-8er' and text()='"+contact"']
selected_contact = driver.find_element_by_xpath("//div[@class='_3Dr46']/span[starts-with(@title,'"+contact+"')]/span[@class='matched-text _3-8er' and text()='"+contact+"']")
actionChains.context_click(selected_contact).perform()
archive_chat_path="//div[@aria-label='Archive chat' and text()='Archive chat']"
if(check_exists_by_xpath(archive_chat_path)):
	driver.find_element_by_xpath(archive_chat_path).click()
back_to_chat=driver.find_element_by_xpath("//span[@data-testid='search']")
if(check_exists_by_xpath(archive_chat_path)):
	back_to_chat.click()
else:
	back_to_chat.click()
	back_to_chat.click()
time.sleep(10)
driver.quit()
