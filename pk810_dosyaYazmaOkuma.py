"""
pk810 — Dosyaya yazma, dosyadan okuma
Önkoşul: pk560 (500 ünitesinin tamamı: string metodları)
Kazanım: open()/write()/read() (with ile) kullanabilir.
kaynak: arsiv/01_9B_2026/305farkliMetodlar.py (dosya kısmı)
"""

# --- KAVRAM ---

# open() bir dosyayı açar. İki temel bilgi verirsin: dosya adı, ve MOD
# ("w" = write/yazma -- dosya yoksa oluşturur, varsa İÇİNİ SİLİP baştan yazar;
#  "r" = read/okuma).

# encoding="utf-8" parametresi ÇOK ÖNEMLİ: onsuz Türkçe karakterler (ş,ğ,ı,ö,ü,ç)
# bozuk kaydedilebilir/okunabilir (Windows varsayılan kodlaması Türkçe
# karakterleri UTF-8 gibi işlemez). Bu yüzden HER dosya açışında yazıyoruz.

# "with ... as dosya:" kalıbı yeni: with, dosyayı açar, blok bitince dosyayı
# OTOMATİK OLARAK KAPATIR -- sen kapatmayı unutsan bile Python halleder.
# (with kullanmadan da dosya açılabilir ama o zaman dosya.close() ile ELLE
# kapatman gerekir, unutmak yaygın bir hatadır -- with bu riski ortadan kaldırır.)

metin = "Python öğrenmek çok eğlenceli!"

with open("ornek.txt", "w", encoding="utf-8") as dosya:
    dosya.write(metin)   # dosyaya metni yazar

# NOT: "ornek.txt" dosyası, bu scripti ÇALIŞTIRDIĞIN KLASÖRE kaydedilir --
# script hangi klasördeyse dosya da ORADA oluşur (masaüstüne ya da rastgele
# bir yere değil). Dosyayı bulamıyorsan, script dosyanla AYNI klasöre bak.

with open("ornek.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()   # dosyanın TÜM içeriğini tek bir string olarak okur
    print("Dosyanın içeriği:", icerik)

# with bloğu bitti -- dosya artık KAPALI, tekrar kullanmak istersen yeniden
# open() etmen gerekir.


# --- SEN YAP ---
# Kullanıcıdan bir cümle al (input ile).
# "notum.txt" adında bir dosyaya (with + encoding="utf-8" ile) bu cümleyi yaz.
# Sonra AYNI dosyayı tekrar aç, oku, içeriğini ekrana yazdır.
# Kullanacağın metod: input(), open(), write(), read(), print()
