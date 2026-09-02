"""
pk150 çözümü — and operatörü + iç içe if karşılaştırması
"""

print("--- and operatörüyle ---")
yas = int(input("Yaşınızı girin: "))
sinav_notu = int(input("Sınav notunuzu girin: "))

if yas >= 15 and sinav_notu >= 60:
    print("Kursa kabul edildin")
else:
    print("Kursa kabul edilmedin")

print("--- iç içe if ile ---")
yas = int(input("Yaşınızı girin: "))
sinav_notu = int(input("Sınav notunuzu girin: "))

if yas >= 15:
    if sinav_notu >= 60:
        print("Kursa kabul edildin")
    else:
        print("Kursa kabul edilmedin")
else:
    print("Kursa kabul edilmedin")
