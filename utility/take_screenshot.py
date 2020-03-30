import datetime
class Takescreenshot():
    def __init__(self,driver):
        self.driver = driver
    def take_screenshot(self):
        screenshot_folder_path = "C:\\Users\\amitg\\Desktop\\screenshots\\"
        self.dirver.save_screenshot(screenshot_folder_path + filename +".png")


    def take_screenshot_with_dynamic_name(self):
        screenshot_folder_path = "C:\\Users\\amitg\\Desktop\\screenshots\\"
        self.dirver.save_screenshot(screenshot_folder_path + str(datetime) + ".png")
