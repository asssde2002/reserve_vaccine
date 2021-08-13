import os

from get_config import get_config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = get_config(PROJECT_DIR)
print(CONFIG.__dict__)

def auto_reservation():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    # Need to make sure the version of your browser and driver is consistent
    driver = webdriver.Chrome('../venv/bin/chromedriver', chrome_options=chrome_options)

    # Choose the vaccination consultation
    driver.get("https://reg.kmuh.gov.tw/netreg/DeptUI.aspx")
    driver.find_element_by_xpath('//*[@id="tContent"]/tbody/tr[6]/td[4]/a').click()
    driver.find_element_by_xpath('//*[@id="divOut"]/table/tbody/tr[4]/td[3]/a').click()
    #[3][6]那邊要改
    
    # Input personal data
    element = driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtPatID")
    element.send_keys(CONFIG["data"]["ID"])
    element = driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtTelNo")
    element.send_keys(CONFIG["data"]["PHONE"])
    element = driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtPatientName")
    element.send_keys(CONFIG["data"]["NAME"])
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_MainContent_rlstGender_1"]').click()
    js="document.getElementById('ctl00_ctl00_MainContent_MainContent_txtBirthday').removeAttribute('readonly')"
    driver.execute_script(js)
    element = driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtBirthday")
    element.clear()
    element.send_keys(CONFIG["data"]["BIRTHDAY"])
    element = driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtAddress")
    element.send_keys(CONFIG["data"]["ADDRESS"])
    driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_MainContent_rbn_covid_qaN"]').click()


#if __name__ == "__main__":
#    auto_reservation()