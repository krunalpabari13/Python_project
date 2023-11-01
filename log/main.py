from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://azure.microsoft.com/en-in/pricing/calculator/")
element_by_class = driver.find_element_by_class_name("text--gray100")