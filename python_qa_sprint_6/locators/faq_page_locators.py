from selenium.webdriver.common.by import By

class FaqPageLocators:

    QUESTION_LOCATOR = By.XPATH, './/div[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//div[@id="accordion__panel-{}"]'