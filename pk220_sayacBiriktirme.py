"""
pk220 — Sayaçla biriktirme
Önkoşul: pk210 (while temel), pk080 (biriktirme girişi)
Kazanım: Sayaç değişkeniyle belirli sayıda tekrar + toplam biriktirme yapabilir.
kaynak: arsiv/01_9B_2026/102birdenOnaKadarToplamSoru.py, arsiv/01_9B_2026/105whileChallenge3Soru.py
"""

# --- KAVRAM ---

# pk080'de "toplam = sayi + toplam" kalıbıyla üç sayıyı ELLE (satır satır) topladık.
# Şimdi aynı kalıbı while İÇİNE koyup, döngü bizim yerimize tekrar etsin:

sayac = 1
toplam = 0
while sayac < 11:
    toplam = toplam + sayac   # pk080'deki biriktirme kalıbı, aynen burada
    sayac = sayac + 1
print("1'den 10'a kadar toplam:", toplam)

# Kısayol: "degisken = degisken + 1" çok sık yazıldığı için Python'da kısa bir
# yazımı var: "degisken += 1". İKİSİ DE TAMAMEN AYNI ŞEYİ yapar, += sadece
# daha az yazmanı sağlar. Aynısı toplama için de var: "toplam += sayac"
# demek "toplam = toplam + sayac" demekle birebir aynıdır.

sayac = 1
toplam = 0
while sayac < 11:
    toplam += sayac   # kısa yazım
    sayac += 1        # kısa yazım
print("Aynı sonuç, kısa yazımla:", toplam)


# --- SEN YAP ---
# Kullanıcıdan bir sayı al (örn. 5).
# while döngüsüyle, o sayıyı KENDİSİ KADAR kere ekrana yazdır
# (5 girilirse beş tane "5" alt alta yazılsın).
# İpucu: bir sayaç değişkeni aç, 0'dan başlat, sayaç kullanıcının girdiği
# sayıya ulaşana kadar döngüde her turda print(sayi) yap ve sayacı += 1 ile artır.
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: <, +=
