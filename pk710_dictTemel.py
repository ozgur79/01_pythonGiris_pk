"""
pk710 — dict nedir, oluşturma
Önkoşul: pk660 (600 ünitesinin tamamı: fonksiyon), pk410 (liste -- karşılaştırma için)
Kazanım: key-value çifti ile dict oluşturabilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# pk410'da listeye SIRA NUMARASI (index) ile erişiyorduk: liste[0], liste[1]...
# dict (sözlük) ise elemanlara ANLAMLI BİR İSİMLE (key/anahtar) erişmeni sağlar.
# Süslü parantez { } içine, "anahtar: değer" çiftleri virgülle ayrılarak yazılır.

ogrenci = {"isim": "Ali", "yas": 15, "sinif": 9}
print(ogrenci)

# Bir değere ulaşmak için köşeli parantez içine ANAHTARI yazarsın (index yerine):
print(ogrenci["isim"])   # "Ali"
print(ogrenci["yas"])    # 15

# liste'de sıra ÖNEMLİYDİ (liste[0] hep ilk elemandı). dict'te anahtar ÖNEMLİDİR,
# sıra değil -- ogrenci["yas"] her zaman yaşı verir, kaçıncı sırada yazdığın
# fark etmez.

# Anahtarlar genelde string olur ama değerler HERHANGİ bir tip olabilir
# (yukarıda "isim" string, "yas" ve "sinif" int değer tutuyor).


# --- SEN YAP ---
# "kitap" adında bir dict oluştur, şu anahtarları içersin: "ad", "yazar", "sayfa".
# Kendi seçtiğin bir kitabın bilgileriyle doldur ("sayfa" int olsun).
# Dict'in tamamını yazdır, sonra "ad" ve "yazar" değerlerini ayrı ayrı yazdır.
# Kullanacağın metod: print()
