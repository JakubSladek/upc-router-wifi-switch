import os
import sys

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from config import config as cfg

class Switch:
    driver = None

    def __init__(self):        
        self.password = cfg.switch["password"]
        self.url = cfg.switch["url"]
        self.headless = cfg.switch["headless"]
        self.geckopath = cfg.switch["geckoPath"]
        self.firefoxpath = cfg.switch["firefoxPath"]

        self.__setupdriver()

    def __setupdriver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.set_headless(headless=self.headless)

        cap = DesiredCapabilities().FIREFOX

        options.binary = self.firefoxpath

        self.driver = webdriver.Firefox(
            capabilities=cap, firefox_options=options, executable_path=self.geckopath)

    def main(self):
        try:
            self._log("started")

            self.driver.get(self.url)
            
            element = self._getelementbyid("loginPassword")
            element.click()
            
            self._log('Trying to log in.')

            element.send_keys(self.password)
            element.send_keys(Keys.RETURN)

            element = self._getelementbyid("c_mu05")
            self._log('Logged on.')
            element.click()

            self._getelementbyid("c_mu06").click()
            self._getelementbyid("c_mu07").click()

            src = self._getelementbyid("iwlanRadio2G1").get_attribute("src")

            if src == '{}images/common_imgs/radio-box-default.png'.format(self.url):
                self._log('Turning on WiFi')
                self._getelementbyid("iwlanRadio2G1").click()
            else:
                self._log('Turning off WiFi')
                self._getelementbyid("iwlanRadio2G2").click()

            self._getelementbyid("c_02").click()

            text = self._getelementbyid("c_72").text

            if text == 'Vaše nastavení bylo uloženo.':
                self._log('Settings successfully saved.')
            else:
                self._log('Something went wrong, please try it again later or contact developer.')

        except Exception as e:
            self._log(e)

        finally:
            if self.driver is not None:
                self.driver.quit()

    def _getelementbyid(self, id):
        return WebDriverWait(self.driver, 1000000).until(EC.element_to_be_clickable((By.ID, id)))

    def _log(self, text):
        print("LOG | {}".format(text))