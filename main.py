from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

#ADD CREDENTIALS HERE
CREDS = {'email' : 'yash.surya2019@vitstudent.ac.in','passwd':'Sagarika@403'}

opt = Options()
opt.add_argument("--disable-infobars")
#opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
#opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })

driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe",options=opt)
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

def start_meeting_test():
    WebDriverWait(driver,1000).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='channel-list-favorites-section-selectable-header']/ul/li[30]")))
    print("meeting starting")
    x=30
    driver.find_element_by_xpath("//*[@id='channel-list-favorites-section-selectable-header']/ul/li["+str(x)+"]").click()
    WebDriverWait(driver,1000).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app-messages-header']/ng-include/div/div/calling-start-button-combo/div[2]/button")))
    driver.find_element_by_xpath("//*[@id='app-messages-header']/ng-include/div/div/calling-start-button-combo/div[2]/button").click()
    print("cam on")
    WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ngdialog1']/div[2]/div/div/div/div[2]/div/calling-new-meetup-overlay/div/div[2]/div[2]/div[1]/toggle-button/div/button/span[1]")))
    driver.find_element_by_xpath("//*[@id='ngdialog1']/div[2]/div/div/div/div[2]/div/calling-new-meetup-overlay/div/div[2]/div[2]/div[1]/toggle-button/div/button/span[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id='ngdialog1']/div[2]/div/div/div/div[2]/div/calling-new-meetup-overlay/div/div[2]/div[2]/div[2]/calling-start-button-rectangular/button").click()

login()
start_meeting_test()
