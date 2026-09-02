"""
pk440 çözümü — while ile liste doldurma
"""

isimler = []
sayac = 0
while sayac < 4:
    isim = input("Bir isim girin: ")
    isimler.append(isim)
    sayac += 1

print(isimler)
