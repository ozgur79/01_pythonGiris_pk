"""
pk080 çözümü — Biriktirme (accumulator) girişi
"""

sayi = int(input("1. sayıyı gir: "))
toplam = sayi
sayi = int(input("2. sayıyı gir: "))
toplam = sayi + toplam
sayi = int(input("3. sayıyı gir: "))
toplam = sayi + toplam
sayi = int(input("4. sayıyı gir: "))
toplam = sayi + toplam

print("Girilen sayıların toplamı:", toplam)
