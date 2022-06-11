import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import datetime
import tempfile
from selenium.webdriver.chrome.options import Options

logfile=tempfile.gettempdir() + "/networkspeed.txt"

options = Options()
options.add_argument('--headless')

def getSpeed ():
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://fast.com/ja/')
    nowdate = datetime.datetime.now()
    wait = WebDriverWait(driver, 10000)
    #処理中が消えるまで待つ
    wait.until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "in-progress")))
    speedvalue = driver.find_element_by_id("speed-value")
    speedunits = driver.find_element_by_id("speed-units")
    speedtext = speedvalue.text + speedunits.text
    logtext = str(nowdate) + ' ' + speedtext
    driver.quit()
    return logtext

ret = getSpeed()
f = open(logfile,'a')
f.write(ret + '\n')
f.close()
