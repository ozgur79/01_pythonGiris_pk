"""
pk650 — Fonksiyona parametre olarak liste, return liste
Önkoşul: pk610 (fonksiyon tanımı, parametre, return), pk450 (for ile liste
doldurma), pk440 (append()'in öğretildiği yer), pk420 (for eleman in liste)
Kazanım: Listeyi parametre alıp for ile işleyip yeni liste return edebilir.
kaynak: arsiv/01_9B_2026/503fonksiyon.py
"""

# --- KAVRAM ---
# Fonksiyona parametre olarak sayı/string değil, DOĞRUDAN bir liste de
# verebilirsin. Bu ders, 600 ünitesi (fonksiyon) ile 400 ünitesini (liste)
# birleştiriyor.

def karelerini_al(sayilar):
    kareler = []                # boş liste (pk440'ı hatırla)
    for sayi in sayilar:        # parametre olarak gelen listeyi for ile gez (pk420)
        kare = sayi * sayi
        kareler.append(kare)    # yeni listeye ekle (pk440'ı hatırla)
    return kareler               # YENİ listeyi geri döndür

sayilar_listesi = [1, 2, 3, 4, 5]
sonuc = karelerini_al(sayilar_listesi)
print("Sayıların kareleri:", sonuc)

# Dikkat: karelerini_al fonksiyonu, verdiğin listeyi DEĞİŞTİRMEDİ -- yeni
# bir liste OLUŞTURUP onu döndürdü. Orijinal liste hâlâ aynı:
print("Orijinal liste hâlâ aynı:", sayilar_listesi)

# Not: Python'da bu işi tek satırda yapmanın da bir yolu var ("list
# comprehension" denir): kareler = [sayi * sayi for sayi in sayilar]
# Bunu şimdi öğrenmene gerek yok -- ileride Python kodlarında görürsen
# şaşırma diye burada gösteriyoruz, sözdizimini bilmen ŞART DEĞİL.


# --- SEN YAP ---
# "pozitifleri_ayikla" adında, tek parametre alan (sayilar) bir fonksiyon
# tanımla. Fonksiyon, gelen listedeki SADECE pozitif sayıları (0 dahil) yeni
# bir listeye ekleyip, o yeni listeyi return etsin.
# En az bir negatif sayı içeren 6 elemanlı bir liste oluştur, fonksiyonu
# çağır, sonucu ekrana yazdır.
# Kullanacağın metod: def, append(), return, print()
# Kullanacağın operatör: >=
