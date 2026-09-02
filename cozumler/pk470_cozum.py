"""
pk470 çözümü — Liste analiz sentezi
"""

notlar = []
kaldi_sayisi = 0
gecti_sayisi = 0
toplam = 0

sayac = 0
while sayac < 4:
    not_puani = int(input("Notu girin: "))
    notlar.append(not_puani)
    if not_puani < 50:
        kaldi_sayisi += 1
    else:
        gecti_sayisi += 1
    toplam += not_puani
    sayac += 1

ortalama = toplam / 4

print("Notlar:", notlar)
print("Kaldı:", kaldi_sayisi)
print("Geçti:", gecti_sayisi)
print("Ortalama:", ortalama)
