"""
pk110 — if temel, girinti, karşılaştırma operatörleri
Önkoşul: pk090 (temel ünitesinin tamamı)
Kazanım: >, <, >=, <=, ==, != ile koşul yazabilir, girintinin blok belirlediğini bilir.
kaynak: arsiv/01_9B_2026/020ifEhliyet.py
"""

# --- KAVRAM ---

# Karşılaştırma operatörleri, iki değeri karşılaştırıp SONUCU True ya da False verir.
print(5 > 3)    # True  (5, 3'ten büyük)
print(5 < 3)    # False (5, 3'ten küçük DEĞİL)
print(5 >= 5)   # True  (5, 5'e eşit ya da büyük)
print(5 <= 4)   # False
print(5 == 5)   # True  (eşit mi? -- DİKKAT: tek "=" değil, ÇİFT "==")
print(5 != 3)   # True  (eşit değil mi?)

# if, bu True/False sonucuna göre kod çalıştırıp çalıştırmayacağına karar verir.
# Koşul True ise if'in ALTINDAKİ (girintili) satırlar çalışır, False ise ATLANIR.

yas = int(input("Yaşınızı girin: "))

if yas >= 18:
    print("Ehliyet alabilir.")       # girinti: bu satır if bloğuna AİT
    print("Dikkatli araba kullan!")  # girinti: bu satır da if bloğuna AİT

print("Programdan çıkıldı...")  # girinti YOK: bu satır if bloğuna AİT DEĞİL, her zaman çalışır

# Girinti (satır başındaki boşluk) süs değil — Python'a "bu satır if'e ait" demenin
# TEK yoludur. Girintiyi bozarsan (eksik ya da tutarsız boşluk) program hata verir.

# Not: "if yas >= 18:" yerine "if (yas >= 18):" yazmak da ÇALIŞIR — parantez
# Python'da if koşulunda ZORUNLU değil (bazı eski kaynaklarda/materyallerde
# parantezli hâlini görebilirsin), ama bu müfredatta parantezsiz yazacağız.


# --- SEN YAP ---
# Kullanıcıdan bir not (0-100 arası bir sayı) al.
# Eğer not 50'den büyük veya 50'ye eşitse "Geçti" yazdır (if bloğunda İKİ satır olsun:
# "Geçti" ve "Tebrikler!").
# if bloğundan sonra, girintisiz bir satırda her zaman "Not kontrolü bitti." yazdır.
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: >=
