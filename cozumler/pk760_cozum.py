"""
pk760 çözümü — Liste içinde dict: kayıt yapısı
"""

kayitlar = []

for i in range(3):
    ad = input("Kitap adı: ")
    sayfa = int(input("Sayfa sayısı: "))
    kitap = {"ad": ad, "sayfa": sayfa}
    kayitlar.append(kitap)

for kitap in kayitlar:
    print(f"{kitap['ad']} ({kitap['sayfa']} sayfa)")
