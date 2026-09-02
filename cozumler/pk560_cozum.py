"""
pk560 çözümü — Pekiştirme: string + for sentezi
"""

kelime = input("Bir kelime girin: ")

sesli_sayaci = 0
for harf in kelime:
    if harf == "a" or harf == "e" or harf == "i" or harf == "ı" or harf == "o" or harf == "ö" or harf == "u" or harf == "ü":
        sesli_sayaci += 1
print("Sesli harf sayısı:", sesli_sayaci)

for harf in kelime:
    print(harf.upper() + "-", end="")
print()
