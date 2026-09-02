"""
pk240 çözümü — continue
"""

while True:
    sayi = int(input("Bir sayı girin (çıkmak için 0 girin): "))
    if sayi == 0:
        print("Bitti")
        break
    if sayi < 0:
        print("Negatif sayıları saymıyorum!")
        continue
    print(sayi * sayi)
