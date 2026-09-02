"""
pk120 — if-else
Önkoşul: pk110 (if temel, girinti, karşılaştırma operatörleri)
Kazanım: İki dallı karar yapısı kurabilir.
kaynak: arsiv/01_9B_2026/021ifEhliyet.py
"""

# --- KAVRAM ---

# pk110'da if koşulu False olunca hiçbir şey OLMUYORDU, direkt sonraki satıra geçiliyordu.
# else, tam olarak "koşul False olduğunda ne olsun" sorusuna cevap verir.
# if VE else, İKİSİNDEN SADECE BİRİ çalışır — asla ikisi birden çalışmaz.

yas = int(input("Yaşınızı girin: "))

if yas >= 18:
    print("Ehliyet alabilir.")       # bu iki satır if bloğuna ait
    print("Dikkatli araba kullan!")
else:
    print("Ehliyet alamaz!")         # bu iki satır else bloğuna ait
    print("Büyüyünce gel :)")

print("Programdan çıkıldı...")  # bu satır if-else yapısının DIŞINDA, her zaman çalışır

# Girinti burada da aynı kuralı takip ediyor: else'in altındaki satırlar else'e ait,
# girintisiz satır ise if-else yapısının tamamına ait değil.


# --- SEN YAP ---
# Kodunda "dogru_sifre" adında bir değişken tanımla, değeri "python2026" olsun.
# Kullanıcıdan input() ile bir şifre al ("girilen_sifre" değişkenine).
# Eğer girilen_sifre, dogru_sifre'ye eşitse "Giriş başarılı" yazdır,
# değilse (else) "Yanlış şifre" yazdır.
# Kullanacağın metod: input(), print()
# Kullanacağın operatör: ==
