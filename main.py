import sqlite3
import os
from get_clean_data import get_product_urls, scrape_product_data, clean_data_list
from config import category, sub_category, product

def connect_to_sqlite_database(db_file):
    # SQLite veritabanına bağlantı oluştur
    conn = sqlite3.connect(db_file)
    return conn

def create_urunler_table(conn):
    # Tabloyu sil
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS urunler")
    
    # Tabloyu yeniden oluştur
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS urunler (
        id INTEGER PRIMARY KEY,
        urun_kodu TEXT,
        base_fiyat REAL,
        urun_bilgileri TEXT,
        urun_hakkinda TEXT,
        resim_url TEXT
    )
    '''
    cursor.execute(create_table_sql)
    conn.commit()

def insert_urun_data(conn, cleaned_data_list):
    # Verileri veritabanına ekleyen SQL sorgusu
    insert_data_sql = '''
    INSERT INTO urunler (urun_kodu, base_fiyat, urun_bilgileri, urun_hakkinda, resim_url)
    VALUES (?, ?, ?, ?, ?)
    '''
    cursor = conn.cursor()

    for product in cleaned_data_list:
        urun_kodu = product['Ürün Kodu']
        base_fiyat = float(product['Base Fiyat'].replace(' TL', '').replace(',', '').strip())
        urun_bilgileri = str(product['Ürün Bilgileri'])
        urun_hakkinda = "\n".join(product['Ürün Hakkında'])  # Liste yerine metin olarak sakla
        resim_url = product['Resim URL']

        cursor.execute(insert_data_sql, (urun_kodu, base_fiyat, urun_bilgileri, urun_hakkinda, resim_url))

    conn.commit()

def close_database_connection(conn):
    conn.close()

if __name__ == "__main__":

#Burada .db uzantlı dosyayı kaydedilecek yeri ve dinamik olarak değişen ismini oluşturduğumuz kısım yer almakta. Son olarak temizlenmiş veri veri tabanına gönderilir ve veritabanı bağlantısı sonlandırılır. 
    # Veritabanı dosyasını kaydetmek istediğiniz dizini belirleyin
    save_directory = r"C:\Users\pc\Desktop\CASE\Database"
    # Veritabanı dosyalarını saklamak istediğiniz dizin yolu
    db_file = os.path.join(save_directory, f"{category}_{sub_category}_{product}.db")  # SQLite veritabanı dosyasının tam yolu

    conn = connect_to_sqlite_database(db_file)
    create_urunler_table(conn)

    urls = get_product_urls()
    product_data_list = []


    for url in urls:
        product_data = scrape_product_data(url)
        product_data_list.append(product_data)

    cleaned_data = clean_data_list(product_data_list)
    print(cleaned_data)
    
    insert_urun_data(conn, cleaned_data)
    close_database_connection(conn)