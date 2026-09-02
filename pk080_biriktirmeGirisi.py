"""
pk080 — Biriktirme (accumulator) girişi
Önkoşul: pk070 (print() içinde değişken/string literal farkı)
Kazanım: Aynı değişkeni güncelleyerek çoklu girdiyi tek değişkende toplayabilir.
kaynak: arsiv/01_9B_2026/013ucSayiIkiDegisken.py
"""

# --- KAVRAM ---

# Şimdiye kadar her sayıyı ayrı bir değişkende tuttuk. Ama üç, dört, beş sayıyı
# toplamak için her seferinde yeni değişken açmak mantıksız olurdu.
# Çözüm: TEK bir "toplam" değişkeni açıp, her yeni sayıyı ona EKLEYEREK güncellemek.
# Bu kalıba "biriktirme" (accumulator) denir — while/for döngülerinde sürekli
# kullanacaksın, burada döngüsüz, elle üç kez tekrar ederek görüyoruz.

sayi = int(input("1. sayıyı gir: "))
toplam = sayi  # toplam, ilk sayıyla başlıyor

sayi = int(input("2. sayıyı gir: "))
toplam = sayi + toplam  # yeni sayı, eski toplama EKLENİYOR

sayi = int(input("3. sayıyı gir: "))
toplam = sayi + toplam  # aynı işlem tekrar

print("Girilen sayıların toplamı:", toplam)

# Dikkat: "sayi" değişkeni her seferinde ÜZERİNE YAZILIYOR (eski değeri kayboluyor),
# ama "toplam" her seferinde ESKİ DEĞERİNİ KORUYARAK üstüne ekliyor.
# Biriktirmenin sırrı tam burada: toplam = ... + toplam (kendi kendini günceller).


# --- SEN YAP ---
# Kullanıcıdan art arda DÖRT sayı al (int(input()) ile, her biri ayrı satırda).
# Bu dört sayıyı "toplam" adlı TEK bir değişkende biriktirerek topla
# (yukarıdaki kalıbı 4 kez tekrarlayarak, döngü kullanmadan).
# Toplamı ekrana yazdır.
# Kullanacağın metod: input(), int(), print()
