from selenium import webdriver
#from time import sleep
from selenium.webdriver.common.by import By

file = open("log.txt", "w")

#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def login():
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    file.write("Success write login\n")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    file.write("Success write password\n")

    login_button = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_button.click()
    file.write("Success click enter\n")


def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK\n")


def test_context_after_login_is_correct():
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK\n")

set_up()
login()
test_login_redirect()
test_context_after_login_is_correct()

file.close()
#driver.quit()