from selenium.webdriver.common.by import By
import time

#Sanity test - open the website and check that it opens
def open_site(driver, url):
    driver.get(url)
    time.sleep(3)
    return driver.current_url

#Enter the website as an existing customer and deposit money into the account
def deposite_money(driver, amount):
    try:
        driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/')
        time.sleep(3)
        driver.maximize_window()
        time.sleep(3)
        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')

        element_button.click()
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, '#userSelect')
        element_button.click()
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, '#userSelect > option:nth-child(4)')
        element_button.click()
        time.sleep(3)
        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > form > button')
        element_button.click()
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
        element_button.click()
        time.sleep(3)

        element_textbox = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
        element_textbox.send_keys(amount)
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
        element_button.click()

        Transaction = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)')
        Transaction.click()
        time.sleep(3)

        return True
    except:
        return False


#Enter the website as an existing customer and deposit money into the account. Then withdraw money from the account.
def deposite_and_withdrawl(driver, amount_to_deposit, amount_to_withdrawl):
    try:
        driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/')
        time.sleep(3)
        driver.maximize_window()
        time.sleep(3)
        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button')
        element_button.click()
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, '#userSelect')
        element_button.click()
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, '#userSelect > option:nth-child(4)')
        element_button.click()
        time.sleep(3)
        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > form > button')
        element_button.click()
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)')
        element_button.click()
        time.sleep(3)

        element_textbox = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
        element_textbox.send_keys(amount_to_deposit)
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
        element_button.click()
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)')
        element_button.click()
        time.sleep(3)

        element_textbox = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input')
        element_textbox.send_keys(amount_to_withdrawl)
        time.sleep(3)

        element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button')
        element_button.click()
        time.sleep(3)


        return True
    except:
        return False

#Enter the website, add a new customer and check if the customer has indeed been added to the customer list.
def add_new_costumer_and_find_him(driver, first_name, last_name, post_code):
    driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/')
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button')
    element_button.click()
    time.sleep(3)

    element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)')
    element_button.click()
    time.sleep(3)

    element_textbox = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input')
    element_textbox.send_keys(first_name)
    time.sleep(3)

    element_textbox = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input')
    element_textbox.send_keys(last_name)
    time.sleep(3)

    element_textbox = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input')
    element_textbox.send_keys(post_code)
    time.sleep(3)

    element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button')
    element_button.click()
    time.sleep(3)

    driver.switch_to.alert.accept()
    time.sleep(3)

    element_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)')
    element_button.click()
    time.sleep(3)

    source = driver.page_source

    if first_name and last_name in source:
        return True
    else:
        return False

