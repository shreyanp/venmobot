from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import schedule
import time

def waitTillDate(spec_date, spec_time):
    #need year, month, day, time
    year = spec_date.year
    month = spec_date.month
    day = spec_date.day
    hour = spec_time.hour
    minute = spec_time.minute


def loginVenmo(number1, password1):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="116.0.5856.96").install()), options=options)

    #number1 = "6126668708"
    #Go to website
    driver.get("https://venmo.com/account/sign-in")
    driver.maximize_window()

    print(number1)
    #Enter in number to begin login and click
    number = driver.find_element(By.ID, "email")
    number.send_keys(number1)
    login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/form/div[3]/button[2]/span")
    login.click()


    #Enter in password to login and click
    password = driver.find_element(By.ID, "password")
    password.send_keys(password1)
    signinfull = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/form/div[4]/button[1]/span")
    signinfull.click()
    
    time.sleep(3)
    #send code fr
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div[3]/button[1]/span").click()
    time.sleep(4)

    return driver

def continuePayment(driver, recipient, code, payAmount, comment=""):
    #If enter code in instead, then: 
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div[2]/form/div/div/input").send_keys(code)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div[3]/button/span").click()

    
    #Say we want to confirm without a code
    #driver.find_element(By.XPATH, "e/html/body/div[1]/div/div[1]/div/div/div/div[3]/a").click()

    time.sleep(2)
    '''
    #If we want to enter in bank account information
    confirminput = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div/div[2]/form/div/div/div/input")
    confirminput.click()
    confirminput.send_keys("9368195864")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div[3]/button[1]").click() #confirm
    '''


    #Do not remember device (not now)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/button[2]").click() 
    time.sleep(2)

    #Pay or Request button
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/nav/div[2]/a[2]/span").click() 

    time.sleep(2)

    #Payment Amount
    payAmt = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div[3]/form/div[1]/div/div/input")
    payAmt.click()
    payAmt.send_keys(payAmount)

    #Enter in username and select
    username = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div[3]/form/div[2]/div/div/div/input")
    username.send_keys(recipient)
    time.sleep(2)
    username.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    username.send_keys(Keys.ENTER)

    #Enter in any comments if wanted
    payNote = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div[3]/form/div[3]/div/div/div/textarea")
    payNote.send_keys(comment)

    time.sleep(2)

    #Pay
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div[3]/form/div[5]/button[1]/span").click()
    time.sleep(5)

    #Confirm pay lol
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div[3]/form/div[5]/div[4]/button[1]/span").click()
    time.sleep(5)

    #If it asks to confirm with last four digits of phone number, skip
    if driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/main/div/div[1]/div[3]/button[1]/span"):
        driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/main/div/div[1]/div[3]/button[1]/span").click()
