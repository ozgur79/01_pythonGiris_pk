"""
pk630 çözümü — Bool döndüren fonksiyon
"""

def pozitif_mi(sayi):
    if sayi >= 0:
        return True
    else:
        return False

sayi = int(input("Bir sayı girin: "))
sonuc = pozitif_mi(sayi)

if sonuc:
    print("Pozitif (veya sıfır)")
else:
    print("Negatif")
