from selenium import webdriver as wd
import time

mail=input("enter your email adsress : ")
pass_mail=input("enter your password : ")
url="https:www.facebook.com"
driver=wd.Chrome(executable_path="C:\\Users\\amitg\\Desktop\\cromedriver\\chromedriver.exe")

driver.get(url)
page_title=driver.title  #"title is a property, so there is no need of parenthesis"
print(page_title)
email_id=driver.find_element_by_id("email")
email_id.send_keys(mail)
password=driver.find_element_by_id("pass")
password.send_keys(pass_mail)

log_in=driver.find_element_by_xpath("//input[@type='submit']")
log_in.click()



driver.maximize_window()


#we need to stop execution for 15 second

time.sleep(4)

log_out_down=driver.find_element_by_xpath("//div[text()='Account Settings']")
log_out_down.click()

log_out_btn=driver.find_element_by_xpath("(//li/a/span/span)[7]")
log_out_btn.click()



#driver.quit()
