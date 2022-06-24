from selenium import webdriver
import time
import json

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")# this is to make the chrome tab will not pop up. the scrapping run in background
