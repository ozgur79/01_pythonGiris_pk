"""
pk640 — Fonksiyon + if-elif-else sentezi
Önkoşul: pk630 (bool döndüren fonksiyon), pk610 (fonksiyon tanımı -- bu derste
elif zinciriyle birleştiriliyor), pk130 (if-elif-else zinciri), pk550 (f-string)
Kazanım: Fonksiyon içinde çok koşullu mantık kurabilir.
kaynak: arsiv/01_9B_2026/genelTekrar03_def.py (arşivde üs alma `num**2`
kullanılmıştı, üs alma hiç öğretilmediği için `num*num` ile değiştirildi)
"""

# --- KAVRAM ---
# Bu ders yeni bir yapı öğretmiyor -- pk130'daki elif zincirini, pk610'daki
# fonksiyon tanımının İÇİNE koyuyoruz.

def sayi_analiz(num):
    if num < 0:
        print(f"Negatif sayı girdiniz: {num}")
    elif num == 0:
        print("Sıfır girdiniz.")
    else:
        print(f"Sonuç: {num * num}")

# Fonksiyonu farklı değerlerle test ediyoruz -- her biri elif zincirinin
# FARKLI bir dalına düşüyor:
sayi_analiz(-5)   # elif'in ilk dalına düşer: negatif
sayi_analiz(0)    # elif'in ikinci dalına düşer: sıfır
sayi_analiz(3)    # else dalına düşer: pozitif, karesi hesaplanır


# --- SEN YAP ---
# "not_degerlendir" adında, tek parametre alan (puan) bir fonksiyon tanımla.
# Fonksiyon içinde if-elif-else zinciriyle (pk130'daki gibi):
#   puan < 50    -> "Kaldı"
#   puan < 70    -> "Orta"
#   puan >= 70   -> "İyi"
# yazdırsın (print ile, fonksiyonun İÇİNDE).
# Fonksiyonu üç farklı puanla (biri her aralıktan) çağır.
# Kullanacağın metod: def, print()
# Kullanacağın operatör: <, >=
