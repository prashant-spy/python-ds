from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def automate_home_page(url, xpath_powerwash_price):
    driver = webdriver.Chrome()
    driver.get(url)
    page_title = driver.title

    homepage_title = "Buy Industrial & Business Supplies Online at the Best Price | Industrybuying"
    if page_title == homepage_title:
        print("we are on home page")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0,1280);")
    product_price_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpath_powerwash_price)))
    product_price_text = product_price_text.text
    print(product_price_text)
    return product_price_text


if __name__ == '__main__':
    url = 'https://www.industrybuying.com/'
    product_price_xpath = '//*[@id="AH_CarouselWidget_60"]/div/div/div[6]/div/a/div[2]/div[1]'
    price_text = automate_home_page(url, product_price_xpath)
    expected = "Rs. 6,790"
    assert price_text, expected
