# name="nagp"
import os
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from pathlib import Path, PurePosixPath


class util():

    def get_driver(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        chrome_location = PurePosixPath(Path.cwd()).joinpath("../chromedriver.exe")
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_location)
        return driver

