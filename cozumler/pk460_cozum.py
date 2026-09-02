"""
pk460 çözümü — Index atamasıyla liste doldurma
"""

liste = [0] * 6
sayac = 0
while sayac < 6:
    liste[sayac] = sayac * sayac
    sayac += 1

print(liste)
