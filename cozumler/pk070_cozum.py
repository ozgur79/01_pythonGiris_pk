"""
pk070 çözümü — print() içinde değişken/string literal farkı
"""

sehir = input("Şehrini gir: ")

print(sehir)     # değişkenin içindeki değeri yazar
print("sehir")   # "sehir" kelimesini olduğu gibi yazar
# Fark: tırnaksız yazınca Python bunu değişken sanıp içindeki DEĞERİ yazdırıyor,
# tırnaklı yazınca ise kelimeyi OLDUĞU GİBİ (literal) yazdırıyor.

print("Şehriniz: " + sehir)
