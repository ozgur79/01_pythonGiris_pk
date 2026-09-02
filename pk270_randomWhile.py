"""
pk270 — random modülü + while
Önkoşul: pk230 (break, sentinel)
Kazanım: random.randint() ile rastgele sayı üretip while ile koşullu üretim yapabilir.
kaynak: arsiv/01_9B_2026/180rasgeleSayi.py, arsiv/01_9B_2026/181rasgeleTekSayiYAP.py
(orijinal 181, "tek sayı" koşulunu % ile kontrol ediyordu; % henüz öğretilmedi
-- pk280'de geliyor -- bu yüzden burada karşılaştırma operatörüyle çalışan bir
koşula uyarlandı: "80'den büyük sayı gelene kadar dene")
"""

# --- KAVRAM ---

# random, Python'ın hazır bir kütüphanesi (bir "araç kutusu"). İçindeki
# randint() fonksiyonu, verdiğin iki sınır arasında rastgele bir tam sayı üretir.
import random

rastgele_sayi = random.randint(1, 100)  # 1 ile 100 arasında (ikisi dahil) rastgele bir sayı
print("Rastgele üretilen sayı:", rastgele_sayi)

# random her çalıştırdığında FARKLI bir sayı verir — programı tekrar çalıştırıp dene.

# Şimdi while ile BİRLEŞTİRELİM: "80'den büyük bir sayı gelene kadar tekrar dene."
rastgele_sayi = 0
while rastgele_sayi <= 80:
    rastgele_sayi = random.randint(1, 100)
    print("Denendi:", rastgele_sayi)

print("80'den büyük sayı bulundu:", rastgele_sayi)

# Burada while'ın koşulu "rastgele_sayi <= 80" — yani sayı 80 ya da altındaysa
# döngü devam eder, YENİ bir rastgele sayı dener. 80'i geçen bir sayı gelince
# koşul False olur, döngü kendiliğinden biter (break'e gerek yok).


# --- SEN YAP ---
# random.randint() ile 1-100 arasında rastgele sayı üretmeye devam eden bir
# while döngüsü kur. Döngü, 30'dan KÜÇÜK bir sayı ÜRETİLENE KADAR sürsün
# (yani sayı 30 ya da üzerindeyse tekrar dene, 30'un altına düşünce dur).
# Her denemede üretilen sayıyı ekrana yazdır.
# Kullanacağın metod: random.randint(), print()
# Kullanacağın operatör: >=
