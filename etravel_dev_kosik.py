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
URL = "https://etravel2.dev.dtweb.cz/egypt/hurghada/hurghada/hurghada-long-beach-resort-ex-hilto?DS=1024&GIATA=26585&D=63484|63485|63483|63486|64421|64419|64422|64420|64425|64423|64426|64424|63232|63247|63249|63250|63251|63257|63280|63289|63325|63326|77802|63361|63381|63332|63401|63450|77804|63461|63528|63527|63526|63529|63470|63205|63212|63215|63229|63255|63265|63271|63287|63296|63298|63329|63330|63339|63436|63356|63391|63404|63406|63410|63422|63425|63426|63429|63444|63453|63454|63456|63457|63459|63539|64427|63538|64428|63537|63720|63724|63723|63721|63719|63717|63722|63715|63718|63716|63582|63581|63580|63208|63222|63343|63395|63419|63466|63220|63219|63209|63262|63281|63283|63285|63290|63297|63311|63314|63316|63319|63324|63383|63333|63336|63341|63352|63362|63364|63384|63387|63388|63390|63402|63408|63409|63428|63430|63442|63471|64439|63399|63214|64435|63266|64433|64438|63327|63335|64442|63357|64441|64431|64437|63424|63427|74677|64436|64432|63431|63437|63439|64440|64434|63685|63472|64087|64094|64095|64089|64090|64088|64091|64086|64092|64096|64093|63213|63226|63231|63241|63242|63243|63244|63245|74462|63267|74459|74460|63284|74461|78291|74463|74464|63350|63354|63360|74465|63455|63216|63218|63227|64429|63263|63272|63299|63334|63313|63328|64430|63363|63252|63447|63260|63288|63448|64154|64152|64153|64157|64103|64125|64098|64105|64101|64100|64102|64124|64097|64123|64099&HID=8719&MT=5&RT=15&NN=7&DF=2021-11-06|2022-01-04&RD=2021-11-21&DD=2021-11-14&AC1=2&KC1=0&IC1=0&DP=4312&TO=4312&TOM=4312&MNN=7&NNM=7&MS=1&PID=1121&DPR=EXIM%20TOURS&ILM=1&IFM=0"
URL_DS1 = "https://etravel2.dev.dtweb.cz/spanelsko/tenerife/puerto-de-la-cruz/globales-acuario?DS=1&GIATA=7086&D=74460|74459|74463|74465&HID=13620&MT=1&DI=49&RT=15&NN=7&DF=2022-07-01|2022-08-31&RD=2022-07-18&DD=2022-07-11&AC1=2&KC1=0&IC1=0&DP=4312&TO=4312&TOM=4312&MNN=7&NNM=7&TT=0&TTM=0&PID=TACU&DPR=Fischer"

driver = webdriver.Chrome(executable_path=r"C:\Users\KADOUN\Desktop\Selenium setup\chromedriver95.exe")
wait = WebDriverWait(driver, 150000)
driver.get(URL_DS1)

time.sleep(2)
acceptConsent(driver)

closeExponeaBanner(driver)
time.sleep(1.5)

koupitZajezd = driver.find_element_by_xpath("//*[@class='c_btn block green mt-4 relative']")
koupitZajezd.click()

time.sleep(5)
acceptConsent(driver)
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

pocetCestujicich=1

time.sleep(20)



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
wait = WebDriverWait(driver, 150000)

osloveni = driver.find_element_by_xpath(passengerOsloveni(pocetCestujicich))
wait.until(EC.visibility_of(osloveni))

osloveni.click()
time.sleep(12)

volbaOsloveni = driver.find_elements_by_xpath("//*[@class='f_input-optionsWrapper js_optionsWrapper'] //*[@class='f_input-option-text']")
volbaOsloveni2 = driver.find_elements_by_xpath("//*[@data-testid='Pan']")
volbaOsloveni3 = driver.find_element_by_xpath("//*[@class='f_customScroll'] //*[@data-testid='Pan']")
volbaOsloveni4 = driver.find_element_by_xpath("//div[@class='f_input-options']//div[@class='f_input-options-content']//div[@data-testid='Pan']")
volbaOsloveni5 = driver.find_element_by_xpath("(//div[@data-testid='Paní'])[1]")
##volbaOsloveni[0].click()
##driver.execute_script("arguments[0].click();", volbaOsloveni3)
time.sleep(4)
##volbaOsloveni2[1].click()

wait.until(EC.element_to_be_clickable(volbaOsloveni5)).click()
time.sleep(2)
potvrditPopup = driver.find_element_by_xpath("(//*[@class='f_button f_button--common f_button_set--small'])[1]")
potvrditPopup.click()



jmenoFirst = driver.find_element_by_xpath(passengerNameFirst(pocetCestujicich))
jmenoFirst.send_keys(name)

jmenoLast = driver.find_element_by_xpath(passengerNameLast(pocetCestujicich))
jmenoLast.send_keys(surname)

