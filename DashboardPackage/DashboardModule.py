from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from cryptography.fernet import Fernet
import pyautogui
import os, sys

driver = None
password = "password"

def setup_driver():
    global driver
    chrome_options = webdriver.ChromeOptions()
    prefs = {"credentials_enable_service", False}
    prefs = {"profile.password_manager_enabled" : False}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument("kiosk")  
#    chrome_options.accept_untrusted_certs = True
#    chrome_options.assume_untrusted_cert_issuer = True
#    chrome_options.add_argument("--no-sandbox")
#    chrome_options.add_argument("--disable-popup-blocking")
#    chrome_options.add_argument("--ignore-certificate-errors")
#    chrome_options.add_argument("--disable-session-crashed-bubble")	
    workDir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    if os.name == "nt":
        driver = webdriver.Chrome(workDir + "/Resources/chromedriver.exe", options=chrome_options)
    else:
        print "Exporting Display..."
        os.environ["DISPLAY"] = ":0.0"
        print "Starting Chrome"        
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=chrome_options)
        pyautogui.FAILSAFE=False
        pyautogui.moveTo(1980, 1080)

def decrypt_password(data):
    split = str(data).split(":")
    f = Fernet(split[0])
    decrypted = f.decrypt(split[1])
    return decrypted
      
def load_settings():
    if len(sys.argv) == 2:        
        global password
        password = decrypt_password(str(sys.argv[1]).replace("-cp ", ""))
        print("Credentials Loaded")
    else:
        print("Missing arguments")

def handle_alert(driver):
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")
        os.system('xdotool key "Escape"')
         
def open_sb_stats():
    print("opening sb stats")    
    driver.get("https://business-tools.stingray.com/apps/sbstats.html")  

def open_grafana():
    print("opening grafana")
    driver.get("https://grafana.business.stingray.com/login")
    element = driver.find_element_by_name("username")
    element.send_keys("jbureau")
    element = driver.find_element_by_name("password")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    handle_alert(driver)
    driver.get("https://grafana.business.stingray.com/d/cSDSMG57k/ad-manager?orgId=1&from=now-3h&to=now&var-Environment=prod&kiosk&autofitpanels")
    
def open_jira():    
    print("opening jira")  
    driver.get("https://jira.corp.stingraydigital.com/secure/Dashboard.jspa")
    element = driver.find_element_by_id("login-form-username")
    element.send_keys("jbureau")
    element = driver.find_element_by_id("login-form-password")
    element.send_keys(password)
    element.send_keys(Keys.RETURN) 
    handle_alert(driver)
    driver.get("https://jira.corp.stingraydigital.com/plugins/servlet/Wallboard/?dashboardId=15608&cyclePeriod=60000&transitionFx=wipe&random=false")


setup_driver()
load_settings()
open_grafana()