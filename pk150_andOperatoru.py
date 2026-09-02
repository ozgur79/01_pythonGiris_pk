"""
pk150 — and operatörü + iç içe if karşılaştırması
Önkoşul: pk120 (if-else)
Kazanım: and ile birleşik koşul yazabilir, aynı mantığı iç içe if ile de kurup
ikisini karşılaştırabilir.
kaynak: arsiv/01_9B_2026/031kullaniciAdiParola.py
"""

# --- KAVRAM ---

# "Hem kullanıcı adı doğru HEM DE şifre doğruysa giriş başarılı" demek istiyoruz.
# Bunu iki farklı yolla yazabiliriz. Önce İÇ İÇE IF ile:

print("--- Yöntem 1: iç içe if ---")
kullanici_adi = input("Kullanıcı adını girin: ")
sifre = input("Parolayı girin: ")

if kullanici_adi == "fatih":
    if sifre == "f1453":              # dıştaki if DOĞRU ise buraya giriyoruz
        print("Başarılı giriş")
    else:
        print("Hatalı giriş (şifre yanlış)")
else:
    print("Hatalı giriş (kullanıcı adı yanlış)")

# İki if iç içe geçince kod hem uzuyor hem de "hangi hata nereden geldi" takip
# etmek zorlaşıyor. Aynı şeyi and operatörüyle TEK satırda yazabiliriz:

print("--- Yöntem 2: and operatörü ---")
kullanici_adi = input("Kullanıcı adını girin: ")
sifre = input("Parolayı girin: ")

if kullanici_adi == "fatih" and sifre == "f1453":
    # and: SOLDAKİ VE SAĞDAKİ koşulun İKİSİ DE True olmalı, yoksa tüm koşul False'tur.
    print("Başarılı giriş")
else:
    print("Hatalı giriş")

# İki yöntem de AYNI SONUCU verir. and ile yazmak daha kısa ama "hangi kısım
# yanlıştı" bilgisini kaybediyoruz (iç içe if'te ayrı ayrı söyleyebiliyorduk).
# Hangisini seçeceğin, ihtiyacına göre değişir.


# --- SEN YAP ---
# Kullanıcıdan yaşını ve sınav notunu (iki ayrı input, int) al.
# Eğer yaş >= 15 VE sınav notu >= 60 ise "Kursa kabul edildin" yazdır,
# değilse "Kursa kabul edilmedin" yazdır.
# Bunu ÖNCE and operatörüyle tek if satırında yaz, sonra AYNI mantığı
# iç içe if ile de yaz (iki farklı program parçası olarak, ikisi de çalışsın).
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: and, >=
