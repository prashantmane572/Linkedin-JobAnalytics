from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import numpy as np


class LinkedIn:
    def __init__(self):
        self.mail = "sohalkhan90570@gmail.com"
        self.password = "JBk1T8[T40}K#(o"

        self.chrome_web = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.chrome_web)

        self.data = {'Designation': [],
                     'Name': [],
                     'Location': [],
                     'Level_and_involvement': [],
                     'Total_applicants': [],
                     'Industry_and_Employee_count': [],
                     'LinkedIn_Followers': []}

    def login(self):
        self.driver.maximize_window()
        self.driver.get('https://www.linkedin.com/')
        mail_box = self.driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[2]/div[1]/input')
        mail_box.send_keys(self.mail)
        password_box = self.driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[2]/div[2]/input')
        password_box.send_keys(self.password)
        login_button = self.driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/button')
        time.sleep(5)
        login_button.click()

    def data_collection(self, link):
        self.driver.get(link)

        bar = self.driver.find_element(By.XPATH, '/html')

        for i in range(1, 21):
            time.sleep(1)
            jobs = self.driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section['
                                                      f'1]/div/ul/li[{i}]/div/div[1]/div[1]/div[2]/div[1]/a')
            time.sleep(1)
            jobs.click()
            time.sleep(1)
            try:
                job_title = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                               '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                               '1]/div/div[1]/div/div[1]/div[1]/a/h2')
                self.data['Designation'].append(job_title.text)
            except NoSuchElementException:
                self.data['Designation'].append(np.nan)
            time.sleep(1)

            try:
                company_name = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                                  '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                                  '1]/div/div[1]/div/div[1]/div[1]/div[1]/span['
                                                                  '1]/span[1]/a')
                self.data['Name'].append(company_name.text)
            except NoSuchElementException:
                self.data['Name'].append(np.nan)
            time.sleep(1)

            try:
                com_location = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                                  '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                                  '1]/div/div[1]/div/div[1]/div[1]/div[1]/span['
                                                                  '1]/span[2]')
                self.data['Location'].append(com_location.text)
            except NoSuchElementException:
                self.data['Location'].append(np.nan)
            time.sleep(1)

            for x in range(4):
                bar.send_keys(Keys.ARROW_DOWN)

            try:
                job_level_and_type = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                                        '4]/div/div/main/div/section[2]/div/div['
                                                                        '2]/div[1]/div/div[1]/div/div[1]/div[1]/div['
                                                                        '2]/ul/li[1]/span')
                self.data['Level_and_involvement'].append(job_level_and_type.text)
            except NoSuchElementException:
                self.data['Level_and_involvement'].append(np.nan)
            time.sleep(1)

            try:
                num_of_applicants = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                                       '4]/div/div/main/div/section[2]/div/div['
                                                                       '2]/div[1]/div/div[1]/div/div[1]/div[1]/div['
                                                                       '1]/span[2]/span[2]/span')
                self.data['Total_applicants'].append(num_of_applicants.text)
            except NoSuchElementException:
                self.data['Total_applicants'].append(np.nan)
            time.sleep(1)

            try:
                com_industry_and_employee_num = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                                                   '4]/div/div/main/div/section['
                                                                                   '2]/div/div[2]/div[1]/div/div['
                                                                                   '1]/div/div[1]/div[1]/div['
                                                                                   '2]/ul/li[2]/span')
                self.data['Industry_and_Employee_count'].append(com_industry_and_employee_num.text)
            except NoSuchElementException:
                self.data['Industry_and_Employee_count'].append(np.nan)
            time.sleep(1)

            sec_bar = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section['
                                                         '2]/div')
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', sec_bar)
            time.sleep(1.5)

            try:
                followers = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div['
                                                               '4]/div/div/main/div/section[2]/div/div[2]/div['
                                                               '1]/div/div[6]/section/section/div[1]/div[1]/div/div['
                                                               '2]/div[2]')
                self.data['LinkedIn_Followers'].append(followers.text)
            except NoSuchElementException:
                self.data['LinkedIn_Followers'].append(np.nan)
            time.sleep(1)

    def create_and_store(self):
        df = pd.DataFrame(self.data)
        df.to_csv('../Data/scrapped data.csv', index=False)


obj = LinkedIn()
obj.login()
flag = [i for i in range(0, 401, 25)]
flag.remove(0)
flag.insert(0, 1)
for i in flag:
    obj.data_collection(f'https://www.linkedin.com/jobs/search/?currentJobId=3365364752&f_C=165158%2C1353%2C58396'
                        f'%2C51692521%2C1283%2C6567943%2C1073%2C18145101%2C12770%2C9215331%2C4300%2C1318%2C3178'
                        f'%2C86813252%2C6339%2C210064%2C14439560&f_E=1%2C2%2C3%2C4%2C5%2C6&geoId=102713980&location'
                        f'=India&refresh=true&start={i}')

obj.create_and_store()
