"""
pk430 — Dilimleme (slicing)
Önkoşul: pk410 (liste nedir, oluşturma, index)
Kazanım: liste[a:b] ile alt liste alabilir.
kaynak: arsiv/01_9B_2026/ssdiziTekrar_Arsivle.py (slicing kısmı)
"""

# --- KAVRAM ---

# pk410'da tek bir elemana index ile ulaşıyorduk (liste[0]). Dilimleme ile
# BİRDEN FAZLA elemanı, YENİ BİR LİSTE olarak tek seferde alabiliriz.

liste = [10, 20, 30, 40, 50]

# liste[a:b]: a'dan başlar, b'ye KADAR gider (b DAHİL DEĞİL) -- range(a,b)'deki
# kuralın AYNISI (pk310'u hatırla).
print(liste[1:4])   # index 1,2,3'ü alır (4 DAHİL DEĞİL) -> [20, 30, 40]
print(liste[0:3])   # index 0,1,2'yi alır (3 DAHİL DEĞİL) -> [10, 20, 30]

# a'yı boş bırakırsan baştan başlar, b'yi boş bırakırsan sona kadar gider:
print(liste[:3])    # baştan başlar, index 3'e kadar -> [10, 20, 30] (liste[0:3] ile aynı)
print(liste[2:])    # index 2'den başlar, sona kadar -> [30, 40, 50]
print(liste[:])     # ikisi de boş -> listenin TAMAMI -> [10, 20, 30, 40, 50]

# Dilim alma, orijinal listeyi DEĞİŞTİRMEZ -- YENİ bir liste üretir.
print("Orijinal liste hâlâ aynı:", liste)


# --- SEN YAP ---
# 7 elemanlı bir sayı listesi oluştur (kendi seçtiğin sayılarla).
# Dilimleme kullanarak:
#   1. İlk 3 elemanı yazdır
#   2. Son 3 elemanı yazdır
#   3. Baştaki VE sondaki elemanı (index 0 ve index 6) hariç, ARADAKİ 5
#      elemanı TEK bir dilimle yazdır (ipucu: liste[1:6])
# Kullanacağın metod: print()
