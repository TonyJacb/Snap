from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def relatedSearch(detectedObject):
    PATH = "/home/tony/SnapKart/tflite/chromedriver"
    driver = webdriver.Chrome(PATH)

    driver.get("https://images.google.com/")

    time.sleep(2)
    element = driver.find_element_by_name("q")
    element.send_keys(detectedObject)
    element.submit()
    time.sleep(5)
