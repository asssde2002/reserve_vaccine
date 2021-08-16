import os
import time
from get_config import get_config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = get_config(PROJECT_DIR)

class Reservation:
    def __enter__(self):   
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(f'{PROJECT_DIR}/venv/bin/chromedriver', chrome_options=chrome_options)
        return self
    
    def __exit__(self ,type, value, traceback):   
        self.driver.close()

    def reserve(self, location):
        # Choose the vaccination consultation
        self.driver.get("https://reg.kmuh.gov.tw/netreg/DeptUI.aspx")
        
        # The field of tr and td may be changed
        self.driver.find_element_by_xpath('//*[@id="tContent"]/tbody/tr[6]/td[4]/a').click()
        self.driver.find_element_by_xpath(f'//*[@id="divOut"]/table/tbody/tr[{location[0]}]/td[{location[1]}]/a').click()
        
        # Input personal data
        element = self.driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtPatID")
        element.send_keys(CONFIG["data"]["ID"])
        element = self.driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtTelNo")
        element.send_keys(CONFIG["data"]["PHONE"])
        element = self.driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtPatientName")
        element.send_keys(CONFIG["data"]["NAME"])
        self.driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_MainContent_rlstGender_1"]').click()
        js = "document.getElementById('ctl00_ctl00_MainContent_MainContent_txtBirthday').removeAttribute('readonly')"
        self.driver.execute_script(js)
        element = self.driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtBirthday")
        element.clear()
        element.send_keys(CONFIG["data"]["BIRTHDAY"])
        element = self.driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$txtAddress")
        element.send_keys(CONFIG["data"]["ADDRESS"])
        self.driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_MainContent_rbn_covid_qaN"]').click()
        self.driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_MainContent_btnSubmit"]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_MainContent_btnConfirm"]').click()
        time.sleep(1)
        
    def check_reservation(self):
        self.driver.get("https://reg.kmuh.gov.tw/netreg/DeptUI.aspx")
        self.driver.find_element_by_xpath('//*[@id="aspnetForm"]/table/tbody/tr[2]/td/div/div[7]/a').click()
        element = self.driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$tbIdno")
        element.send_keys(CONFIG["data"]["ID"])

        element = self.driver.find_element_by_name("ctl00$ctl00$MainContent$MainContent$tbChartNo")
        birthday = CONFIG["data"]["BIRTHDAY"].split('/')
        year = f"{int(birthday[0]) - 1911:03d}"
        month = birthday[1]
        day = birthday[2]
        element.send_keys(year+month+day)
        
        self.driver.find_element_by_xpath('//*[@id="ctl00_ctl00_MainContent_MainContent_btnSubmit"]').click()
        time.sleep(0.5)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        soup = soup.find("table", class_="table02").find("td")
        reserved_result = soup.get_text()
        if reserved_result == "查無預約掛號的資料！":
            return "Failed"
        return "Successful"
    

if __name__ == "__main__":
    result = "Failed"
    available_field = (3, 4)
    
    with Reservation() as r:
        for i in range(2):
            r.reserve(available_field)
            result = r.check_reservation()
            with open(f"{PROJECT_DIR}/execution.log", "a") as fp:
                fp.write(f"Reserved Result: {result}\n")
                
            if result == "Successful":
                break
            time.sleep(1)
    
        
