"""
pk140 — if-elif pratik, farklı senaryo
Önkoşul: pk130 (if-elif-else zinciri)
Kazanım: elif zincirini farklı bir problemde (string karşılaştırmalı) tekrar kurabilir.
kaynak: arsiv/01_9B_2026/032hesapMakinesiCevapBITMEDI.py (arşivde sözdizimi hatası vardı:
elif(*): ve elif(/): geçersizdi, kodlar placeholder'dı — bu script tamamlanmış hali)
"""

# --- KAVRAM ---

# pk130'daki elif zinciri SAYI aralıklarını karşılaştırıyordu. Bu sefer STRING
# karşılaştıracağız — mantık birebir aynı, sadece karşılaştırdığımız değer string.

sayi1 = int(input("1. sayıyı girin: "))
sayi2 = int(input("2. sayıyı girin: "))
islem_tipi = input("İşlem tipini seçin (+ - * /): ")

if islem_tipi == "+":
    sonuc = sayi1 + sayi2
    print("Sayıların toplamı:", sonuc)
elif islem_tipi == "-":
    sonuc = sayi1 - sayi2
    print("Sayıların farkı:", sonuc)
elif islem_tipi == "*":
    sonuc = sayi1 * sayi2
    print("Sayıların çarpımı:", sonuc)
elif islem_tipi == "/":
    # Dikkat: sayi2'ye 0 girersen bu satır ÇÖKER (ZeroDivisionError).
    # Matematikte de sıfıra bölme tanımsızdır, Python da bunu hata sayar.
    # Bunu şimdi denemeni öneririz: 2. sayı olarak 0 gir, gerçek hatayı gör.
    # pk045'i hatırla: traceback'in EN ALT satırı "ZeroDivisionError: division
    # by zero" diyecek. Bu ders o hatayı ÖNLEMEYİ değil, TANIMAYI öğretiyor —
    # önleme (if ile kontrol etme) ileride göreceğin bir konu.
    sonuc = sayi1 / sayi2  # / böler, sonucu HER ZAMAN ondalıklı (float) verir
    print("Sayıların bölümü:", sonuc)
else:
    print("Yanlış işlem tipi girdiniz.")


# --- SEN YAP ---
# Kullanıcıdan bir gün adı al (input ile, örn. "pazartesi").
# if-elif-else zinciriyle:
#   "pazartesi", "sali", "carsamba", "persembe", "cuma" girilirse -> "Hafta içi"
#   "cumartesi", "pazar" girilirse -> "Hafta sonu"
#   başka bir şey girilirse -> "Geçersiz gün"
# İpucu: her gün için ayrı bir elif satırı yazabilirsin, ya da "and"/"or"
# henüz görmediğin için (pk150/pk160'ta gelecek) şimdilik her günü tek tek kontrol et.
# Kullanacağın metod: input(), print()
# Kullanacağın operatör: ==
