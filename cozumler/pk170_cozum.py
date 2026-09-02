"""
pk170 çözümü — Pekiştirme: and ile bağımsız pratik
"""

sinav_notu = int(input("Sınav notunuzu girin: "))
devamsizlik = int(input("Devamsızlık gün sayınızı girin: "))

if sinav_notu >= 50 and devamsizlik <= 10:
    print("Sınıfı geçti")
else:
    print("Sınıfı geçemedi")
