from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        # self.wait = wait

    CLICK_ON_MY_ACCOUNT_XPATH = (By.XPATH,"//*[@title='My Account']")
    CLICK_ON_LOGIN_LINK_TEXT = (By.LINK_TEXT,"Login")
    ENTER_EMAIL_ADDRESS_XPATH = (By.CSS_SELECTOR,"[id='input-email']")
    ENTER_PASSWORD_TEXT_BOX_XPATH = (By.CSS_SELECTOR,"[id='input-password]")
    ClICK_ON_LOGIN_BUTTON_XPATH = (By.XPATH,"//*[@class='btn btn-primary'][@value= 'Login']")
    # wait = WebDriverWait(self.driver,10)

    def login_to_the_application_with_valid_credentials(self,user_name,password):
        global wait
        wait = WebDriverWait(self.driver,10)
        my_account = wait.until(EC.visibility_of_element_located(self.CLICK_ON_MY_ACCOUNT_XPATH))
        my_account.click()

        login_link = wait.until(EC.visibility_of_element_located(self.CLICK_ON_LOGIN_LINK_TEXT))
        login_link.click()

        enter_email = wait.until(EC.visibility_of_element_located(self.ENTER_EMAIL_ADDRESS_XPATH))
        enter_email.send_keys(user_name)
        enter_password = wait.until(EC.visibility_of_element_located(self.ENTER_PASSWORD_TEXT_BOX_XPATH))
        enter_password.send_keys(password)
        click_login = wait.until(EC.visibility_of_element_located(self.ClICK_ON_LOGIN_BUTTON_XPATH))
        click_login.click()

