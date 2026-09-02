"""
pk060 — Değişkende ara sonuç saklama
Önkoşul: pk040 (int() dönüşümü, sayısal toplam)
Kazanım: Değişkende hesap sonucunu saklayıp tekrar kullanabilir.
kaynak: arsiv/01_9B_2026/010degiskenKaresi.py
"""

# --- KAVRAM ---

# Bir hesabın sonucunu bir değişkende SAKLAYABİLİRİZ, sonra o değişkeni
# başka bir işlemde tekrar kullanabiliriz. Sonucu hemen print() etmek zorunda değiliz.

sayi = int(input("Karesi alınacak sayıyı gir: "))
karesi = sayi * sayi  # sonuç burada hesaplanıp "karesi" değişkeninde saklandı
print("Girilen sayının karesi:", karesi)

# "karesi" değişkeni hâlâ hafızada duruyor, onu başka bir hesapta da kullanabiliriz:
karesinin_iki_kati = karesi * 2
print("Karenin iki katı:", karesinin_iki_kati)

# Dikkat: "sayi" değişkenini YENİDEN kullanırsak, eski değeri kaybolur.
sayi = sayi + 10  # artık "sayi" eski değeri değil, 10 fazlasını tutuyor
print("Sayıya 10 eklenmiş hali:", sayi)


# --- SEN YAP ---
# Kullanıcıdan bir kenar uzunluğu al (int).
# Bu kenarla oluşan karenin alanını (kenar*kenar) bir değişkende sakla.
# Aynı değişkeni kullanarak karenin çevresini de (kenar*4) ayrı bir değişkende sakla.
# İkisini de ekrana yazdır.
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: *
