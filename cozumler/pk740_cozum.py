"""
pk740 çözümü — for ile dict gezme
"""

notlar = {"Ali": 70, "Veli": 45, "Ayşe": 90}

for isim in notlar:
    if notlar[isim] < 50:
        print(isim + ": Kaldı")
    else:
        print(isim + ": Geçti")
