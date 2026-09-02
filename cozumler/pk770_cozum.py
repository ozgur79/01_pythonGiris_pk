"""
pk770 çözümü — dict ile sayma/gruplama
"""

cumle = input("Bir cümle girin: ")
sayac = {}

for karakter in cumle:
    if karakter in sayac:
        sayac[karakter] += 1
    else:
        sayac[karakter] = 1

for karakter in sayac:
    print(karakter, ":", sayac[karakter])
