from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome (executable_path="C:\\Users\\Sanket\\Desktop\\sele_python\\webdriver\\chromedriver.exe")
driver.get("https://jqueryui.com/")
driver.maximize_window()
sortable_link=driver.find_element_by_xpath("//a[text()='Sortable']")
sortable_link.click()
sleep(3)
driver.switch_to.frame(0)
actions=ActionChains(driver)
sortable_items=driver.find_element_by_xpath("(//ul[@id='sortable']/li)[1]")

#sortable_drag=driver.find_element_by_xpath("(//ul[@id='sortable']/li)[1]")
#sortable_drop=driver.find_element_by_xpath("(//ul[@id='sortable']/li)[7]")
actions=ActionChains(driver)
#actions.drag_and_drop(sortable_drag,sortable_drop).perform()
actions.drag_and_drop_by_offset(sortable_items,0,300).perform()
sleep(5)
driver.close()
driver.quit()
