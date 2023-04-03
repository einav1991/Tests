from selenium import webdriver

from bank_tests.main import *


class TestBank:
    #The test checks if the website opens
    def test_sanity(self):
        driver = webdriver.Chrome(r'C:\Users\Shir\Downloads\chromedriver\chromedriver.exe')
        expected = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
        actual = open_site(driver, expected)
        assert expected == actual

    #The test checks if the money the customer deposited in the account actually appears in the account.
    def test_deposite_250(self):
        driver = webdriver.Chrome(r'C:\Users\Shir\Downloads\chromedriver\chromedriver.exe')
        url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
        open_site(driver, url)
        actual = deposite_money(driver, 250)
        expected = True
        assert expected == actual

    #The test checks if the balance is accurate after depositing money into the account and withdrawing money from the account.
    def test_deposite_and_withdrawl(self):
        driver = webdriver.Chrome(r'C:\Users\Shir\Downloads\chromedriver\chromedriver.exe')
        url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
        open_site(driver, url)
        actual = deposite_and_withdrawl(driver, 1000, 250)
        print("actual "+ str(actual))
        expected = True
        print("expected " + str(expected))
        assert expected == actual

    # The test checks if the new customer I added is actually in the customer list.
    def test_add_new_costumer_and_find_him(self):
        driver = webdriver.Chrome(r'C:\Users\Shir\Downloads\chromedriver\chromedriver.exe')
        url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
        open_site(driver, url)
        actual = add_new_costumer_and_find_him(driver, 'Severus', 'Snape', 1234)
        expected = True
        assert expected == actual

