from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os
from config import category, sub_category, product, data_directory, json_file_name


def initialize_browser():
    #Bu fonksiyon web tarayıcıyı aktif eder ve boyutunu belirler.
    browser = webdriver.Chrome()
    browser.set_window_size(1000, 800)
    return browser

def click_category(browser, cat, sub_cat, product_name):

    #Bu fonksiyon config.py dosyasından girilen category, sub_cat ve product değişkenlerini kullanarak ilgili kategoriye tıklama işlemi yapar. 

    # Kategori seçimini yapmak için XPath ifadesini oluştur
    xpath_expression = f"//a[contains(text(),'{cat}')]"
    sub_xpath_expression = f"//a[contains(text(),'{sub_cat}')]"
    product_xpath_expression = f"//div[contains(@class, 'menu__main--item-link-text') and text()='{product_name}']"

    try:
        # Kategoriye tıkla
        element = browser.find_element(By.XPATH, xpath_expression)
        element.click()
        sub_element = browser.find_element(By.XPATH, sub_xpath_expression)
        sub_element.click()
        time.sleep(3)
        product_element = browser.find_element(By.XPATH, product_xpath_expression)
        product_element.click()
    except Exception as e:
        print("Aradığınız kategori bulunamadı.")

def get_product_urls(browser):

    #Bu fonksiyon ürün sayfasına ulaştıktan sonra ürünlerin tek tek adreslerini alarak product_urls adlı listeye kaydeder.

    time.sleep(5)
    product_urls = []
    while True:
        product_links = browser.find_elements(By.CSS_SELECTOR, "#product-fill div.product-card__image a")
        for link in product_links:
            product_url = link.get_attribute("href")
            product_urls.append(product_url)
        
        try:
            # Daha fazla göster düğmesini bulun
            load_more_button = browser.find_element(By.CSS_SELECTOR, "#product-container > div.load-more > button")
            # Daha fazla göster düğmesi tıklanabilir olana kadar bekle
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-container > div.load-more > button")))
            time.sleep(3)
            
            # Daha fazla göster düğmesine tıkla
            #load_more_button.click()
            browser.execute_script("arguments[0].click();", load_more_button)
            
            time.sleep(5)  # Yükleme işleminin tamamlanmasını beklemek için daha uzun bir süre
        except Exception as e:
            print(f"Daha fazla ürün yükleme butonuna tıklanamadı: {e}")
            break

    return product_urls

def save_product_urls(product_urls, directory, file_name):

#Bu fonksiyon product_urls adlı listeyi alarak, ürünlerin adreslerini belirtilen yola, ismi dinamik olarak belirlenerek json uzantılı olarak kaydeder.
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        json.dump(product_urls, file)
    
def main():

    #Burada adresler .json uzantılı dosya olarak kaydediliyor. Kayıt edilecek adres config.py dosyasından seçilebilir.

    browser = initialize_browser()
    url = "https://www.defacto.com.tr/"
    browser.get(url)
    
    click_category(browser, category, sub_category, product)
    time.sleep(3)

    product_urls = get_product_urls(browser)

    for url in product_urls:
        print(url)

    save_product_urls (product_urls, data_directory, json_file_name)

    print(product_urls)

    browser.quit()

if __name__ == "__main__":
    main()