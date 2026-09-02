"""
pk090 çözümü — Pekiştirme: temel ünitesi karma
"""

# --- Problem 1 ---
isim = input("İsminizi girin: ")
dogum_yili = int(input("Doğum yılınızı girin: "))
yas = 2026 - dogum_yili
print(isim, yas, "yaşındadır.")

print("---")

# --- Problem 2 ---
sayi = int(input("1. sayıyı girin: "))
toplam = sayi
sayi = int(input("2. sayıyı girin: "))
toplam = sayi + toplam
sayi = int(input("3. sayıyı girin: "))
toplam = sayi + toplam
sayi = int(input("4. sayıyı girin: "))
toplam = sayi + toplam
ortalama = toplam / 4

print("Toplam:", toplam)
print("Ortalama:", ortalama)
