"""
pk540 — String indexleme ve dilimleme
Önkoşul: pk410 (liste index), pk430 (liste dilimleme)
Kazanım: Liste ile paralel olarak string'i index/slice edebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# pk410'da liste[index], pk430'da liste[a:b] öğrenmiştik. String'ler de AYNI
# kurallarla index'lenir ve dilimlenir -- string'i "harflerden oluşan bir liste"
# gibi düşünebilirsin.

metin = "Python"

print(metin[0])    # ilk harf: P
print(metin[-1])   # son harf: n (negatif index, pk410'daki gibi)
print(metin[0:3])  # index 0,1,2 -- "Pyt" (3 DAHİL DEĞİL, pk430'daki kural aynen geçerli)
print(metin[3:])   # index 3'ten sona kadar -- "hon"

# Fark: listede bir index'in değerini DOĞRUDAN DEĞİŞTİREBİLİRSİN:
liste = [10, 20, 30]
liste[0] = 99   # var olan elemanın üzerine yazıyoruz, bu ÇALIŞIR
print(liste)

# String'de bu ÇALIŞMAZ -- string "değiştirilemez" (immutable) bir veri
# tipidir. metin[0] = "J" yazmaya çalışırsan TypeError alırsın (bu satır
# yorumda bırakıldı, çalıştırmıyoruz):
#   metin[0] = "J"   # TypeError: 'str' object does not support item assignment


# --- SEN YAP ---
# Kullanıcıdan bir kelime al (input ile, en az 4 harfli olsun).
# Şunları ekrana yazdır:
#   1. Kelimenin ilk harfi (index 0)
#   2. Kelimenin son harfi (negatif index)
#   3. Kelimenin ilk 2 harfi (dilimleme ile)
#   4. Kelimenin son 2 harfi (dilimleme ile)
# Kullanacağın metod: input(), print()
