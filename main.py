from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

##cant figure out how to select osloveni in the popup box so stucked on that

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
        exponeaBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']")
        if exponeaBanner.is_displayed():

            wait.until(EC.visibility_of(exponeaBanner))
            exponeaCrossAndBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']//*[@class='exponea-close']")
            exponeaCrossAndBanner.click()
            time.sleep(2)

    except NoSuchElementException:
        print( "nenasle se exponea banner")

def acceptConsent(driver):
    def expand_shadow_element(element):
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root
    try:
        outer = expand_shadow_element(driver.find_element_by_css_selector("div#usercentrics-root"))
        inner = outer.find_element_by_css_selector("button[data-testid='uc-accept-all-button']")
        inner.click()
    except NoSuchElementException:
        pass

name = "Ondřej"
surname = "Tester"
email = "ondrej.kadoun@fischer.cz"
phone = "735599725"
URL = "https://dev.eximtours.cz/recko/rhodos/faliraki/hotel-fantasia-resor?DS=1024&GIATA=183926&D=63220|63316|63319|63324|63333|63402|63409|63471&HID=9336&MT=2&RT=15&NN=7&RD=2021-10-06&DD=2021-09-29&DP=4312&MNN=7|8|9&TT=1&PID=6851&DPR=EXIM%20TOURS&TTM=1&DF=2021-09-29|2021-10-30&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0#"

driver = webdriver.Chrome(executable_path=r"C:\Users\KADOUN\Desktop\Selenium setup\chromedriver93.exe")
wait = WebDriverWait(driver, 150000)
driver.get(URL)

time.sleep(1)
acceptConsent(driver)

closeExponeaBanner(driver)
time.sleep(1.5)

mamZajem = driver.find_element_by_xpath("//*[@class='fshr-bubble-wrapper']")
mamZajem.click()

time.sleep(5)
firstNameKO = driver.find_element_by_xpath("//*[@name='customer.firstName']")
lastNameKO = driver.find_element_by_xpath("//*[@name='customer.lastName']")
emailKO = driver.find_element_by_xpath("//*[@name='customer.email']")
phoneKO = driver.find_element_by_xpath("//*[@name='customer.phoneNumber']")

wait.until(EC.visibility_of(firstNameKO))
firstNameKO.send_keys(name)
lastNameKO.send_keys(surname)
emailKO.send_keys(email)
phoneKO.send_keys(phone)

time.sleep(1)
pokracovatKO = driver.find_element_by_xpath("//*[@data-testid='nextStep']")

pokracovatKO.click()

pocetCestujicich=2

time.sleep(4)

##functiosn for returning locator based on how many ppl are there
##the locators have test names and are same expect the number of the traveler so makes sense to do it in this way
##then just while loop pocetceustjicih >2 and send the values to all of it

def passengerOsloveni(pocetCestujicich):
    pocetCestujicich = str(pocetCestujicich)
    locator = "//*[@name='room.0.passenger." + pocetCestujicich + ".salutation']"
    print(locator)
    return locator

def passengerNameFirst(pocetCestujicich):
    pocetCestujicich = str(pocetCestujicich)
    locator = "//*[@name='room.0.passenger." + pocetCestujicich + ".name.first']"
    print(locator)
    return locator

def passengerNameLast(pocetCestujicich):
    pocetCestujicich = str(pocetCestujicich)
    locator = "//*[@name='room.0.passenger." + pocetCestujicich + ".name.last']"
    print(locator)
    return locator




osloveni = driver.find_element_by_xpath(passengerOsloveni(pocetCestujicich))
osloveni.click()
time.sleep(5)
##muzall locates two elements so tried for loop to click on both of them
##err selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
muzAll = driver.find_elements_by_xpath("//*[@class='f_input-optionsWrapper js_optionsWrapper'] //*[@data-testid='Muž'and not(@style='display: none;')]")
driver.execute_script("arguments[0].click();", muzAll)
muzAll.click()
for _ in muzAll:
    muzSingle = driver.find_element_by_xpath("//*[@class='f_customScroll'] //*[@data-testid='Muž'and not(@style='display: none;')]")
    driver.execute_script("arguments[0].click();", muzSingle)
    muzSingle.click()


jmenoFirst = driver.find_element_by_xpath(passengerNameFirst(pocetCestujicich))
jmenoFirst.send_keys(name)

jmenoLast = driver.find_element_by_xpath(passengerNameLast(pocetCestujicich))
jmenoLast.send_keys(name)

