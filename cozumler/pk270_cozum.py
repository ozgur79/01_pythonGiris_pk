"""
pk270 çözümü — random modülü + while
"""

import random

rastgele_sayi = 100
while rastgele_sayi >= 30:
    rastgele_sayi = random.randint(1, 100)
    print("Denendi:", rastgele_sayi)

print("30'un altında sayı bulundu:", rastgele_sayi)
