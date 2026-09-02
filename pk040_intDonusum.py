"""
pk040 — int() dönüşümü, sayısal toplama
Önkoşul: pk020 (input, string birleştirme)
Kazanım: int(input()) ile sayısal veri alıp aritmetik işlem yapabilir.
kaynak: arsiv/01_9B_2026/003intToplama.py
"""

# --- KAVRAM ---

# input() her zaman STRING döndürür — sayı gibi görünse bile.
sayi1_string = input("1. sayıyı gir: ")
print("Bu aslında bir string, kanıtı:", sayi1_string * 2)  # string 2 kere yazılır, çarpılmaz

# int() bir string'i tam sayıya (integer) çevirir.
# Artık matematiksel işlem yapabiliriz.
sayi1 = int(sayi1_string)
print("Şimdi int oldu, kanıtı:", sayi1 * 2)  # gerçekten 2 ile çarpıldı

# Genelde bu iki adım (input + int) tek satırda birleştirilir:
sayi2 = int(input("2. sayıyı gir: "))

toplam = sayi1 + sayi2
print("Sayıların toplamı:", toplam)

# Uyarı: string + string birleştirir, int + int toplar. İkisini KARIŞTIRAMAZSIN.
# "5" + "3" -> "53"   (string birleştirme)
#  5  +  3  -> 8      (sayısal toplama)


# --- SEN YAP ---
# Kullanıcıdan üç ayrı sayı al (int(input()) ile).
# Bu üç sayının toplamını ve ortalamasını hesaplayıp ekrana yazdır.
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: +, / (ortalama için toplamı 3'e böl)
