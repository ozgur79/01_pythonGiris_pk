"""
pk160 — or operatörü
Önkoşul: pk150 (and operatörü + iç içe if karşılaştırması)
Kazanım: or ile "ikisinden biri yeterli" koşulunu yazabilir.
kaynak: arsiv/01_9B_2026/ss03.py
"""

# --- KAVRAM ---

# and'de İKİ koşulun da True olması gerekiyordu. or'da ise TERSİ: koşullardan
# HERHANGİ BİRİ True ise (ikisi birden de olabilir), tüm koşul True sayılır.

cevap = input("İstiklal Marşı şairimizin soyadı nedir? ")

if cevap == "ersoy" or cevap == "Ersoy" or cevap == "ERSOY":
    # or: soldaki, ortadaki, sağdaki koşullardan HERHANGİ BİRİ True ise yeter.
    # Kullanıcı küçük harf, büyük harf ya da baş harfi büyük yazmış olabilir,
    # üçünü de "doğru" saymak için üç kez or ile karşılaştırıyoruz.
    print("Bildin")
else:
    print("Bilemedin")

# Karşılaştırma: and yazsaydık ("ersoy" or "Ersoy" or "ERSOY" AYNI ANDA hiçbir
# zaman doğru olamaz, çünkü kullanıcı tek bir şey yazar) — bu yüzden burada
# doğru operatör or'dur, and DEĞİL. Hangi operatörü seçeceğin, "ikisi birden mi
# gerekli (and) yoksa biri yeterli mi (or)" sorusuna verdiğin cevaba bağlı.


# --- SEN YAP ---
# Kullanıcıya "Bugün ne yapmak istersin? (kitap/film/oyun) " diye sor.
# Eğer cevap "kitap" VEYA "film" ise "İyi seçim, dinlendirici olur." yazdır.
# Değilse (else) "Farklı bir tercih." yazdır.
# Kullanacağın metod: input(), print()
# Kullanacağın operatör: or, ==
