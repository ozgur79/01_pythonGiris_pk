"""
pk090 — Pekiştirme: temel ünitesi karma
Önkoşul: pk010-pk080 (temel ünitesinin tamamı)
Kazanım: Ünitedeki tüm kalıpları (input, dönüşüm, birleştirme, biriktirme) bağımsız yazabilir.
kaynak: arsiv/01_9B_2026/014Soru.py, arsiv/01_9B_2026/015Soru.py
"""

# --- KAVRAM ---
# Bu ders yeni bir şey ÖĞRETMİYOR — 000 ünitesindeki her şeyi tek bir örnekte
# bir araya getiriyor. Aşağıdaki kod, önceki 8 dersin (pk010-pk080) hepsinden
# birer parça içeriyor. Çalıştır, satır satır hangi dersten geldiğini tanımaya çalış.

isim = input("İsminizi girin: ")               # pk020: input(), string
dogum_yili = int(input("Doğum yılınızı girin: "))  # pk040: int() dönüşümü

yas = 2026 - dogum_yili                         # pk060: değişkende sonuç saklama
print(isim, yas, "yaşındadır.")                 # pk030: birden çok değeri print() ile yazdırma

print(isim)     # pk070: değişken -> içindeki değer yazılır
print("isim")   # pk070: string literal -> olduğu gibi yazılır

# pk080: biriktirme -- ikişer ikişer üç kere sayı alıp toplama
sayi = int(input("1. sayıyı girin: "))
toplam = sayi
sayi = int(input("2. sayıyı girin: "))
toplam = sayi + toplam
sayi = int(input("3. sayıyı girin: "))
toplam = sayi + toplam
print("Girilen sayıların toplamı:", toplam)


# --- SEN YAP ---
# Aşağıdaki iki problemi, her biri AYRI bir program parçası olarak (yukarıdaki
# KAVRAM kodunu kopyalamadan, sıfırdan) çöz. Cevap burada YOK, sadece problem
# tanımı ve kullanacağın değişken/metod listesi var — arşivdeki 014Soru.py ve
# 015Soru.py'nin izinden gidiyoruz.

# --- Problem 1 ---
# Kullanıcının ismi ve doğum yılı bilgisi alınacak,
# ekrana "<isim> <yaş> yaşındadır." şeklinde bilgi mesajı yazdırılacak.
#
# Değişkenler:
#   isim        # string
#   dogum_yili  # integer
#   yas         # integer
# Metodlar:
#   input(), int(), print()

# --- Problem 2 ---
# Klavyeden girilen DÖRT sayıyı (üç değil, dört — pk080'den bir adım fazlası)
# toplayan ve ORTALAMASINI da hesaplayan bir program yaz.
#
# Değişkenler:
#   sayi     # integer, her seferinde üzerine yazılır
#   toplam   # integer, biriktirilir
#   ortalama # toplam / 4
# Metodlar:
#   input(), int(), print()
