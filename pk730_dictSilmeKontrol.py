"""
pk730 — Silme, key kontrolü
Önkoşul: pk720 (erişim, ekleme, güncelleme)
Kazanım: del, in operatörüyle key varlığını kontrol edip silebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

ogrenci = {"isim": "Ali", "yas": 15, "sinif": 9, "okul": "Fen Lisesi"}

# del: bir anahtar-değer çiftini dict'ten TAMAMEN SİLER
del ogrenci["okul"]
print("Silindikten sonra:", ogrenci)

# in: bir anahtarın dict'te OLUP OLMADIĞINI kontrol eder, True/False döndürür
# (pk730'a kadar in'i hiç görmedin -- bu yeni bir operatör)
print("isim" in ogrenci)      # True, çünkü "isim" anahtarı var
print("okul" in ogrenci)      # False, çünkü az önce sildik

# in'i if ile birleştirerek, silmeden/okumadan ÖNCE anahtarın var olup
# olmadığını kontrol edebilirsin -- bu, pk720'nin sonundaki KeyError riskini
# ÖNLER:
if "telefon" in ogrenci:
    print("Telefon:", ogrenci["telefon"])
else:
    print("Telefon bilgisi kayıtlı değil.")

# del ile var OLMAYAN bir anahtarı silmeye çalışırsan da hata alırsın --
# bu yüzden silmeden önce in ile kontrol etmek iyi bir alışkanlıktır.


# --- SEN YAP ---
# pk720'deki "kitap" dict'ini (ad, yazar, sayfa, yil) yeniden oluştur.
# Şunları yap:
#   1. "yil" anahtarının dict'te olup olmadığını in ile kontrol et, sonucu yazdır
#   2. "sayfa" anahtarını del ile sil
#   3. Silme işleminden sonra "sayfa" anahtarının hâlâ olup olmadığını in ile
#      tekrar kontrol et, sonucu yazdır (artık False çıkmalı)
# Kullanacağın metod: print()
# Kullanacağın operatör: in
