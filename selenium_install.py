#@title Instalacion de paquetes
!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

#@title Configuracion de Selenium Browser
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
browser.get("https://www.webite-url.com")
## https://stackoverflow.com/questions/56829470/selenium-google-colab-error-chromedriver-executable-needs-to-be-in-path

width =   400 #@param {type:"integer"}
height =   768 #@param {type:"integer"}
# Rezising
browser.set_window_size(width, height)
browser.maximize_window()
