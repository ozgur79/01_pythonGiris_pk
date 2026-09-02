"""
pk030 — Çoklu string birleştirme
Önkoşul: pk020 (yorum satırı, string birleştirme, input)
Kazanım: Birden çok string değişkeni + ile anlamlı bir cümlede birleştirebilir; print()
içinde virgülün ne yaptığını bilir.
kaynak: arsiv/01_9B_2026/002stringToplama2.py
"""

# --- KAVRAM ---

# pk020'de iki string'i birleştirmiştik. Şimdi ÜÇ VEYA DAHA FAZLA string'i
# tek bir cümlede birleştireceğiz. Mantık aynı, sadece + sayısı artıyor.

il = "Sivas "
ilce = "Kangal "
mahalle = "Cennet "

# Aralarına elle yazdığımız kelimeleri de (" ilinde ", " ilçesindeki " gibi)
# katarak tek bir okunaklı cümle kuruyoruz.
adres = il + "ilinde " + ilce + "ilçesindeki " + mahalle + "mahallesine gidecek"

# print()'e virgülle birden fazla şey verebilirsin — bu, + İLE AYNI ŞEY DEĞİL.
# print(a, b) yazınca Python a'yı yazar, ARAYA KENDİLİĞİNDEN BİR BOŞLUK KOYAR, sonra b'yi yazar.
# + ise iki string'i OLDUĞU GİBİ yapıştırır, boşluk eklemez (istersen sen elle eklersin).
print("Kargo adresi:", adres)   # virgül -> "Kargo adresi:" ile adres arasına boşluk KENDİLİĞİNDEN girer
print("Kargo adresi:" + adres)  # + ile aynısını yazsaydık, arada boşluk OLMAZDI (bitişik yazardı)

# Değişkenlerin sırasını değiştirmek cümlenin anlamını da değiştirir —
# string birleştirme sırayla yapılır, Python kendiliğinden düzeltmez.
adres2 = mahalle + "mahallesi, " + ilce + "ilçesi, " + il + "ili"
print("Kargo adresi (farklı sırayla):", adres2)


# --- SEN YAP ---
# Kullanıcıdan sırasıyla "ad", "soyad" ve "meslek" bilgisini input() ile al.
# Bu üç bilgiyi + ile birleştirip şu formatta tek bir cümle yazdır:
#   "<ad> <soyad>, mesleği <meslek> olan biridir."
# Kullanacağın metod: input(), print()
# Kullanacağın operatör: + (en az 3 kez)
