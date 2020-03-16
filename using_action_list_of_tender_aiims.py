from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.by import By

driver =webdriver.Chrome(executable_path="C:\\Users\\amitg\\Desktop\\cromedriver\\chromedriver.exe")
driver.get("https://www.aiims.edu/en.html")
print(driver.title)
driver.maximize_window()
sleep(5)
action = ActionChains(driver)
tender=driver.find_element(By.XPATH,'//li[@id="menu-629"]')

AWARD_LETTER=driver.find_element(By.ID,'menusys676')
sleep(5)
action.move_to_element(tender).move_to_element(AWARD_LETTER).click().perform()
sleep(3)


tender_titles=driver.find_elements_by_xpath("//tbody/tr/td/a")
print("Number_of_tender::",len(tender_titles))

title_list=[]
for title in tender_titles:
    title_list.append(title.text)
    print("TITLE:",title.text)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("=",title_list)
sleep(10)
driver.quit()
