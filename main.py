import logging
import os
import requests
import time

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from urllib.parse import urlencode, quote_plus
from pathlib import Path

#Setzen der Variablen
inputpath = os.environ.get('INPUTPATH', '/tmp/home')
telegrambotkey = os.environ.get('TELEGRAMBOTKEY')
chatid = os.environ.get('CHATID')

logger = logging.getLogger("bonavendi")
logger.setLevel(logging.INFO)
fh = logging.StreamHandler()
fh.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)


eans = "0600753339886\n5050466796820"

logger.info(eans)
logger.info(inputpath)

opts = Options()
opts.headless = True
logger.info("Starte FireFox")
browser = Firefox(options=opts)

try:
    logger.info("Öffne Startseite")

    # Startseite
    browser.get('https://www.bonavendi.de/verkaufen/sammeleingabe.html')
    time.sleep(10)
    try:
        browser.get_screenshot_as_file(inputpath + "/1.png")
    except WebDriverException:
        logger.warning("Bild 1 konnte nicht gespeichert werden.")

    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/div/div/textarea").send_keys(eans)
    logger.info("EANs eingetragen")
    time.sleep(10)
    try:
        browser.get_screenshot_as_file(inputpath + "/2.png")
    except WebDriverException:
        logger.warning("Bild 2 konnte nicht gespeichert werden.")

    browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div/div/button").click()
    logger.info("EANs submittet")

    # Seite nach EAN Eingabe
    time.sleep(30)
    try:
        browser.get_screenshot_as_file(inputpath + "/3.png")
    except WebDriverException:
        logger.warning("Bild 3 konnte nicht gespeichert werden.")

    browser.get("https://www.bonavendi.de/verkaufen/korb.html")
    time.sleep(20)

    try:
        browser.get_screenshot_as_file(inputpath + "/4.png")
    except WebDriverException:
        logger.warning("Bild 4 konnte nicht gespeichert werden.")

    text = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div[2]/div/h2/span").text
    logger.info(text)

except Exception as inst:
    print("Fehler in der Verarbeitung:", inst)
finally:
    browser.quit()

exit(0)