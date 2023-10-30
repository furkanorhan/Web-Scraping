# Web-Scraping
-Projenin çalıştırılması-
Öncelikle ilgili kategorileri ve .json uzantılı dosyanın kaydedileceği yeri config.py dosyasında belirledikten sonra, create_json.py isimli dosyaya geliyoruz. Bu kodu çalıştırdığımızda belirttiğimiz dizinde json dosyası oluşuyor.
Daha sonra main.py dosyasının çalıştırılmasıyla, verilerimiz .db uzantılı dosyaya kaydediliyor. Bu dosyayı görüntülemek için DB Browser kullanılabilir.

-Not:
Öncelikle proje için bir arayüz planlamıştım, streamlit üzerinden butona bastıktan sonra kullanıcıdan alınan kategori ve ürün verileri .json uzantılı dosya oluşturulmak için kullanılacak. Daha sonra ise verilerin web sitesinden çekilip .db uzantılı dosya olarak kaydedilecekti.
Daha sonra da yine arayüz üzerinden .db uzantılı dosyayı kullanıp verileri görselleştirme gibi işlevleri de test etmek istemiştim fakat streamlit kullanırken sürekli chome driver hatası aldım bu yüzden arayüz düşüncesinden vazgeçtim.
Bir diğer kısım ise .json uzantılı dosya oluşturmadan direkt url vererek de verileri çekebilirdim fakat test etmek uzun süreceği ve bu uygulama fazla yük oluşturacağı için 2 kısımda yapmaya karar verdim. Eğer istenirse birleştirilebilir.
Yaklaşık 1.5 gündür resimleri indirmeye çalışıyorum fakat bir türlü beceremedim, resmin adresini websitesinden alabiliyorum fakat indirmeye gelince indiremiyorum. Basit bir işlem olduğunu biliyorum fakat bir türlü çözemedim.
Son olarak ise neredeyse istenilen her veri websitesinden çekilebildiğini gördüm ve ihtiyaca göre düzenlenebilir ben test için son durumda bu şekilde bıraktım.

Proje için 4 gün yaklaşık 6-7 saat uğraştım ve 1dk bile sıkıldığımı hatırlamıyorum. Böyle bir fırsat verdiğiniz için teşekkür ederim. İyi çalışmalar. 
