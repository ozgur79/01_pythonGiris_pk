"""
pk630 — Bool döndüren fonksiyon
Önkoşul: pk610 (fonksiyon tanımı, parametre, return), pk280 (% operatörü),
pk110 (karşılaştırma operatörlerinin True/False döndürdüğü yer)
Kazanım: Fonksiyondan True/False döndürüp çağıran tarafta if ile kullanabilir.
kaynak: arsiv/01_9B_2026/502fonksiyon.py
"""

# --- KAVRAM ---

# pk110'da karşılaştırma operatörlerinin (5>3 gibi) sonucunun True/False
# olduğunu görmüştük. Bir fonksiyon da return ile DOĞRUDAN True ya da False
# döndürebilir -- bu, "evet/hayır" cevabı veren fonksiyonlar için idealdir.

def cift_mi(sayi):
    if sayi % 2 == 0:
        return True
    else:
        return False

sayi = int(input("Analiz edilecek sayıyı girin: "))
sonuc = cift_mi(sayi)   # sonuc artık True ya da False tutuyor

# Bir boolean (True/False) değişkeni, if'in koşuluna DOĞRUDAN yazılabilir --
# "if sonuc == True:" yazmana GEREK YOK, "if sonuc:" yeterli:
if sonuc:
    print("Çift sayıdır.")
else:
    print("Tek sayıdır.")

# Fonksiyonu print() içinde DOĞRUDAN da kullanabilirsin, ara değişken şart değil:
print("7 çift mi?", cift_mi(7))
print("10 çift mi?", cift_mi(10))


# --- SEN YAP ---
# "pozitif_mi" adında, tek parametre alan (sayi) bir fonksiyon tanımla.
# Fonksiyon, sayi 0 veya 0'dan büyükse True, değilse False döndürsün.
# Kullanıcıdan bir sayı al, fonksiyonu çağır, sonucu bir değişkende tut.
# if ile o değişkeni kontrol edip "Pozitif (veya sıfır)" ya da "Negatif" yazdır.
# Kullanacağın metod: def, return, input(), int(), print()
# Kullanacağın operatör: >=
