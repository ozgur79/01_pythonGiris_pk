"""
pk070 — print() içinde değişken/string literal farkı
Önkoşul: pk060 (değişkende ara sonuç saklama)
Kazanım: print(isim) ile print("isim") arasındaki farkı ayırt edebilir
(yaygın başlangıç hatası).
kaynak: arsiv/01_9B_2026/011degiskenIsimYil.py
"""

# --- KAVRAM ---

isim = input("İsminizi girin: ")  # "isim" değişkeni string tutuyor
yil = int(input("Doğum yılınızı girin: "))  # "yil" değişkeni int tutuyor

yas = 2026 - yil
print(isim, yas, "yaşındadır")

# ÇOK ÖNEMLİ FARK — bu dersin asıl konusu:
print(isim)     # tırnaksız -> Python bunu bir DEĞİŞKEN sanır, içindeki DEĞERİ yazar
print("isim")   # tırnaklı  -> Python bunu bir STRING LITERAL sanır, harfi harfine "isim" yazar

print(yil)       # değişkenin içindeki değeri yazar (örn. 2011)
print("yil")     # olduğu gibi "yil" kelimesini yazar

# Kural: tırnak varsa Python onu OLDUĞU GİBİ yazar (metin).
# Tırnak yoksa Python onu bir isim (değişken) sanıp, o isme bağlı DEĞERİ arar.
# "yil" adında bir değişken yoksa bu NameError verirdi (pk045'i hatırla).


# --- SEN YAP ---
# "sehir" adında bir değişkene input() ile bir şehir ismi al.
# Sonra art arda dört satır yaz:
#   1. print(sehir)      -> değişkenin değerini yazdırsın
#   2. print("sehir")    -> "sehir" kelimesini olduğu gibi yazdırsın
#   3. Aralarındaki farkı açıklayan bir yorum satırı ekle
#   4. Kullanıcıya "Şehriniz: " ile başlayan, sehir değişkenini içeren bir cümle yazdır
# Kullanacağın metod: input(), print()
