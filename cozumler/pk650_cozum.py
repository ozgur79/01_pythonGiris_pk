"""
pk650 çözümü — Fonksiyona parametre olarak liste, return liste
"""

def pozitifleri_ayikla(sayilar):
    pozitifler = []
    for sayi in sayilar:
        if sayi >= 0:
            pozitifler.append(sayi)
    return pozitifler

sayilar_listesi = [5, -3, 8, -1, 0, -7]
sonuc = pozitifleri_ayikla(sayilar_listesi)
print(sonuc)
