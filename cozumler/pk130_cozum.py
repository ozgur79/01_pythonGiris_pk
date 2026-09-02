"""
pk130 çözümü — if-elif-else zinciri
"""

yas = int(input("Yaşınızı girin: "))

if yas < 0:
    print("Geçersiz yaş")
elif yas < 13:
    print("Çocuk")
elif yas < 18:
    print("Genç")
elif yas < 65:
    print("Yetişkin")
else:
    print("Yaşlı")
