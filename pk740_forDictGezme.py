"""
pk740 — for ile dict gezme
Önkoşul: pk730 (silme, key kontrolü), pk420 (for eleman in liste), pk720
(dict[anahtar] ile değere erişim)
Kazanım: for ile bir dict'in tüm anahtarlarını gezip her anahtarın değerine
ulaşabilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# pk420'de "for eleman in liste" ile listenin elemanlarını tek tek gezmiştik.
# "for" ile dict de gezilebilir -- ama DİKKAT: dict'i for ile gezersen,
# değişkenine DEĞERLER değil ANAHTARLAR gelir.

ogrenci = {"isim": "Ali", "yas": 15, "sinif": 9}

for anahtar in ogrenci:
    print(anahtar)   # sadece "isim", "yas", "sinif" yazar -- değerler DEĞİL

# Değere ulaşmak istiyorsan, pk720'deki dict[anahtar] kalıbını anahtar ile
# birlikte kullanman gerekir:
for anahtar in ogrenci:
    print(anahtar, "->", ogrenci[anahtar])

# Not: dict'lerle çalışırken .keys(), .values(), .items() diye üç ayrı metod
# da SIKÇA görülür (internette/ileri kaynaklarda karşına çıkabilir). Biz
# burada onları öğretmiyoruz -- yukarıdaki "for anahtar in dict" + "dict[anahtar]"
# kalıbı, zaten bildiğin araçlarla (pk420, pk720) TAMAMEN aynı işi görür.


# --- SEN YAP ---
# "notlar" adında bir dict oluştur, üç öğrencinin adını anahtar, sınav notunu
# (int) değer olarak tut (örn. {"Ali": 70, "Veli": 45, "Ayşe": 90}).
# for ile dict'i gez, her öğrenci için:
#   notu 50'den küçükse "<isim>: Kaldı" yazdır
#   değilse "<isim>: Geçti" yazdır
# Kullanacağın metod: print()
# Kullanacağın operatör: <
