"""
pk530 çözümü — split(), strip()
"""

cumle = input("Boşluklu bir cümle girin: ")
kelimeler = cumle.split()
print("Kelime sayısı:", len(kelimeler))

kelime = input("Başında/sonunda boşluk olan bir kelime girin: ")
print("[" + kelime.strip() + "]")
