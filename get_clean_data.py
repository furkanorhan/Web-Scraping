import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import requests
from config import json_file_path
import os
import json


def get_product_urls():

#Bu fonksiyon .json dosyasını bularak içerisindeki adres bilgilerini product_urls isimli listeye kaydeder ve product_urls isimli listeyi döner.
    
    if os.path.exists(json_file_path):
        print(f"JSON dosyası bulundu: {json_file_path}")
    else:
        print(f"JSON dosyası bulunamadı: {json_file_path}")

    # JSON dosyasının okunarak product_urls isimli listeye kaydedilmesi.

    with open(json_file_path, "r") as file:
        product_urls = json.load(file)

    return product_urls

def scrape_product_data(url):
    try:
        # Tarayıcıyı başlat
        browser = webdriver.Chrome()
        browser.set_window_size(1300, 1200)

        # Ürün sayfasını ziyaret et
        browser.get(url)

        # Sayfa içeriğini analiz et
        soup = BeautifulSoup(browser.page_source, "html.parser")
        product_price_base = soup.find("div", class_="product-card__price--new d-inline-flex align-items-baseline").text
        product_code = soup.find("div", class_="product-card__code").text.strip()

        # Resmin URL'sini alın
        img_tag = browser.find_element(By.CSS_SELECTOR, '#product-main-container > div.product > div > div.product-card > div > div > div.col-12.col-md-8.col-lg-9.p-0.product-card__left > div > div > div.product-card__image-slider--container.swiper-container > div > div:nth-child(1) > div > img')
        image_url = img_tag.get_attribute("data-src")

        # Eğer URL bir şema içermiyorsa, ekleyin
        if not image_url.startswith('http'):
            image_url = 'https:' + image_url

        # "Devamını Gör" düğmesini tıkla
        continue_button = browser.find_element(By.CLASS_NAME, "productinfo-trigger")
        browser.execute_script("arguments[0].click();", continue_button)

        # İçeriğin yüklenmesini bekleyin (örneğin, 5 saniye)
        time.sleep(5)

        # Şimdi içeriği çekin
        wait = WebDriverWait(browser, 10)
        product_info_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#section__productinfo > div.sideMenu__container > div > div:nth-child(1) > ul")))
        product_info = product_info_element.text
        about_product_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#section__productinfo > div.sideMenu__container > div > div:nth-child(2) > ul > li:nth-child(1)")))
        about_product = about_product_element.text

        # Tarayıcıyı kapat
        browser.quit()

        return {
            'Ürün Kodu': product_code,
            'Base Fiyat': product_price_base,
            'Ürün Bilgileri': product_info,
            'Ürün Hakkında': about_product,
            'Resim URL': image_url
        }
    except Exception as error:
        print(f"Hata oluştu: {error}")
        return None

def clean_data_list(data_list):
    cleaned_data_list = []

    for data in data_list:
        cleaned_data = {
            'Ürün Kodu': data['Ürün Kodu'],
            'Base Fiyat': data['Base Fiyat'],
            'Ürün Bilgileri': data['Ürün Bilgileri'],
            'Ürün Hakkında': data['Ürün Hakkında'],
            'Resim URL': data['Resim URL']
        }
        cleaned_data_list.append(cleaned_data)

    return cleaned_data_list

if __name__ == "__main__":
   
    #TEST
    print("null")
    #product_df = create_dataframe(product_data_list,urls)
    #print(product_df)
