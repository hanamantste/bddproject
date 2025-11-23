from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Shopping:
    def __init__(self,driver):
        self.driver = driver

    add_to_cart_button = (By.XPATH,"//*[text()='Add to Cart']")
    add_to_cart = (By.XPATH,"//*[@id='button-cart']")
    click_item = (By.XPATH,"//*[@id='cart']")
    check_out = (By.XPATH,"//*[@class='text-right']//*[contains(@href,'index.php?route=checkout/checkout')]")
    check_out_options = (By.CSS_SELECTOR,"[href='#collapse-checkout-option']")



    def add_cart_button(self):
        global wait
        wait = WebDriverWait(self.driver,20)
        wait.until(EC.visibility_of_element_located(self.add_to_cart_button)).click()
        wait.until(EC.visibility_of_element_located(self.add_to_cart)).click()

    def click_cart(self):
        wait.until(EC.visibility_of_element_located(self.click_item)).click()


    def check_out_cart(self):
        wait.until(EC.visibility_of_element_located(self.check_out)).click()

