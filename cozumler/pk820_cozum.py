"""
pk820 çözümü — Dosyayı satır satır okuma
"""

liste_metni = """Ekmek
Süt
Yumurta
Peynir"""

with open("alisveris.txt", "w", encoding="utf-8") as dosya:
    dosya.write(liste_metni)

with open("alisveris.txt", "r", encoding="utf-8") as dosya:
    kalemler = dosya.readlines()

for kalem in kalemler:
    print("-", kalem, end="")
print()
