"""
pk520 — upper(), lower()
Önkoşul: pk510 (len(), find()), pk160 (or operatörü)
Kazanım: String'i büyük/küçük harfe çevirebilir.
kaynak: arsiv/01_9B_2026/305farkliMetodlar.py (upper, lower kısmı)
"""

# --- KAVRAM ---

metin = "Python Programlama"
print(metin.upper())   # tüm harfleri BÜYÜK yapar
print(metin.lower())   # tüm harfleri küçük yapar

# --- pk160'a geri dönelim ---
# pk160'ta kullanıcının "ersoy", "Ersoy" ya da "ERSOY" yazmasını üç ayrı or
# ile karşılıyorduk:

cevap = input("İstiklal Marşı şairimizin soyadı nedir? ")

if cevap == "ersoy" or cevap == "Ersoy" or cevap == "ERSOY":
    print("Bildin (eski yöntem -- pk160'taki hâli)")

# .lower() ile kullanıcının YAZDIĞI HER ŞEYİ küçük harfe çevirip TEK bir
# karşılaştırma yapabiliriz -- kullanıcı nasıl yazarsa yazsın sonuç aynı:

if cevap.lower() == "ersoy":
    print("Bildin (yeni yöntem -- .lower() ile)")

# İki yöntem de AYNI GİRDİLER için AYNI SONUCU verir, ama .lower() ile üç kez
# or yazmaya gerek kalmadı. Metod, tanımından değil, ÇÖZDÜĞÜ SIKINTIDAN
# anlaşılıyor: pk160'ta çektiğimiz "üç kere yazma" derdi burada bitiyor.


# --- SEN YAP ---
# Kullanıcıdan bir şehir adı al ("hangi şehirde yaşıyorsun?" gibi bir soru sor).
# .lower() kullanarak, kullanıcı ister büyük ister küçük harfle yazsın,
# cevabın "sivas" olup olmadığını TEK bir karşılaştırmayla kontrol et.
# "sivas" ise "Memleketim!" yazdır, değilse "Farklı bir şehir." yazdır.
# Kullanacağın metod: input(), lower(), print()
