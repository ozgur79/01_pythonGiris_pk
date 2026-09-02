"""
pk720 — Erişim, ekleme, güncelleme
Önkoşul: pk710 (dict nedir, oluşturma)
Kazanım: dict[key] ile okuyup yazabilir, yeni key ekleyebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

ogrenci = {"isim": "Ali", "yas": 15, "sinif": 9}

# GÜNCELLEME: var olan bir anahtarın değerini değiştirmek -- eski değerin
# ÜZERİNE yazıyorsun, anahtar aynı kalıyor:
ogrenci["sinif"] = 10
print("Güncellenmiş:", ogrenci)

# EKLEME: dict'te henüz olmayan bir anahtara değer atarsan, dict OTOMATİK
# OLARAK büyür, yeni anahtar-değer çifti eklenir:
ogrenci["okul"] = "Fen Lisesi"
print("Yeni anahtar eklendi:", ogrenci)

# Dikkat: syntax İKİSİ İÇİN DE AYNI (dict["anahtar"] = deger) -- Python,
# anahtar zaten VARSA günceller, YOKSA ekler. Sen ayrım yapmak zorunda değilsin.

# Var olmayan bir anahtarı OKUMAYA çalışırsan (yazmaya değil), hata alırsın:
#   print(ogrenci["telefon"])   # KeyError: 'telefon' (yorumda bırakıldı, çalıştırmıyoruz)


# --- SEN YAP ---
# pk710'daki "kitap" dict'ini (ad, yazar, sayfa) yeniden oluştur.
# Şunları yap:
#   1. "sayfa" değerini güncelle (kitabı yeniden okudun, sayfa sayısını
#      yanlış girmiştin diyelim, düzelt)
#   2. "yil" adında YENİ bir anahtar ekle (kitabın basım yılı, int)
# Her adımdan sonra dict'in güncel hâlini yazdır.
# Kullanacağın metod: print()
