from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

#ADD CREDENTIALS HERE
CREDS = {'email' : 'yash.surya2019@vitstudent.ac.in','passwd':'Sagarika@403'}

driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.microsoft.com/en-in/microsoft-teams/log-in")
print("browser up")
driver.find_element_by_xpath("//*[@id='office-Hero5050-zdjhwg8']/section/div/div[1]/div/div/div/div/div[1]/a").click()

#SWITCH TO TAB2
driver.switch_to.window(driver.window_handles[1])

def login():
    global driver
    print("logging in")
    WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.ID, "i0116")))
    emailField=driver.find_element_by_id('i0116')
    emailField.click()
    emailField.send_keys(CREDS['email'])
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()  # Next button
    WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.ID, "i0118")))
    passwordField = driver.find_element_by_xpath("//*[@id='i0118']")
    passwordField.click()
    passwordField.send_keys(CREDS['passwd'])
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()  # Sign in button
    WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='idSIButton9']")))
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()  # remember login
    print("logged in")

def start_meeting():

    WebDriverWait(driver,1000).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='channel-list-favorites-section-selectable-header']/ul/li[30]")))
    print("meeting starting")
    driver.find_element_by_xpath("//*[@id='channel-list-favorites-section-selectable-header']/ul/li[30]").click()
    WebDriverWait(driver,1000).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app-messages-header']/ng-include/div/div/calling-start-button-combo/div[2]/button")))
    driver.find_element_by_xpath("//*[@id='app-messages-header']/ng-include/div/div/calling-start-button-combo/div[2]/button").click()
    print("cam on")

login()
start_meeting()
