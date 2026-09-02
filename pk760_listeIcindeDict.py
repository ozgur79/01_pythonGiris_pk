"""
pk760 — Liste içinde dict: kayıt yapısı
Önkoşul: pk750 (basit uygulama: sözlük/rehber), pk450 (for ile liste doldurma),
pk410 (liste), pk710 (dict), pk420 (for eleman in liste)
Kazanım: Kayıt yapısını (öğrenci bilgisi gibi) liste + dict ile modelleyebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# pk410'da sade bir liste ([10,20,30]) gördük, pk710'da tek bir dict
# ({"isim":"Ali",...}) gördük. Şimdi ikisini birleştiriyoruz: bir LİSTE,
# elemanları DICT olan bir yapı. Bu, birden çok "kayıt"ı (her biri birkaç
# bilgi içeren) bir arada tutmanın standart yoludur.

ogrenciler = [
    {"isim": "Ali", "puan": 70},
    {"isim": "Veli", "puan": 45},
    {"isim": "Ayşe", "puan": 90},
]

# Dıştaki for, listenin her ELEMANINI (yani her dict'i) gezer -- pk420'deki
# "for eleman in liste" ile birebir aynı, sadece eleman burada bir dict:
for ogrenci in ogrenciler:
    print(ogrenci["isim"], "->", ogrenci["puan"])

# İçindeki her dict'e normal şekilde erişebilirsin -- listenin ilk elemanı
# (index 0) bir dict olduğu için, ["isim"] ile onun içine inebilirsin:
print("İlk öğrencinin ismi:", ogrenciler[0]["isim"])


# --- SEN YAP ---
# Boş bir liste oluştur (kayitlar).
# for ve range() kullanarak (pk450'deki gibi) kullanıcıdan TAM 3 kitap bilgisi
# al: her tur için "ad" ve "sayfa" (int) bilgisini input ile al, bunlardan
# bir dict oluştur ({"ad": ..., "sayfa": ...}), append() ile kayitlar
# listesine ekle.
# Döngü bitince, kayitlar listesini for ile gez ve her kitabı
# "<ad> (<sayfa> sayfa)" formatında yazdır.
# Kullanacağın metod: input(), int(), append(), print()
