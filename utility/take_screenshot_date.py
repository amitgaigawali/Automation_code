import datetime
from time import time
import random
class Takescreenshot():
    def __init__(self,driver):
        self.driver = driver
    def take_screenshot(self,filename):
        screenshot_folder_path = "C:\\Users\\amitg\\Desktop\\screenshots\\"
        self.driver.save_screenshot(screenshot_folder_path +filename +".png")


    def take_screenshot_with_dynamic_name(self):
        screenshot_folder_path = "C:\\Users\\amitg\\Desktop\\screenshots\\"
        #filename = round(random.random()*1000)
        
        file_name = datetime.datetime.fromtimestamp(round(time()))
        #file_name= round(time())
        self.driver.save_screenshot(screenshot_folder_path+str(file_name)+".png")
