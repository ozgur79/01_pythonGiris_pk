"""
pk440 — while ile liste doldurma
Önkoşul: pk430 (dilimleme), pk230 (break, sentinel)
Kazanım: while döngüsünde append() ile listeyi doldurabilir, birden fazla
çözüm yolunu karşılaştırabilir.
kaynak: arsiv/01_9B_2026/ssdiziTekrar_Arsivle.py (mirsad/selim kod kısmı)
"""

# --- KAVRAM ---

# Şimdiye kadarki listelerimizi HAZIR yazdık (liste = [10,20,30]). Ama genelde
# listeyi PROGRAM ÇALIŞIRKEN, adım adım DOLDURMAK isteriz. Bunun için:
#
#   liste.append(deger)
#
# metodunu kullanırız. append(), verdiğin değeri listenin EN SONUNA ekler,
# listeyi BİR ELEMAN BÜYÜTÜR.

liste = []          # BOŞ bir liste ile başlıyoruz
liste.append(10)    # liste artık: [10]
liste.append(20)    # liste artık: [10, 20]
liste.append(30)    # liste artık: [10, 20, 30]
print(liste)

# --- Şimdi bunu while ile OTOMATİKLEŞTİRELİM: kullanıcıdan 5 sayı topla ---
liste = []
sayac = 0
while sayac < 5:
    sayi = int(input("Bir sayı girin: "))
    liste.append(sayi)   # her turda listeye BİR ELEMAN eklenir
    sayac += 1
print("Girilen liste:", liste)

# --- Aynı problemi FARKLI bir sentinel yaklaşımıyla da çözebiliriz ---
# ("0 girilene kadar topla" -- pk280'deki sentinel kalıbının liste hali)
liste2 = []
while True:
    sayi = int(input("Bir sayı girin (bitirmek için 0 girin): "))
    if sayi == 0:
        break
    liste2.append(sayi)
print("Girilen liste (sentinel ile):", liste2)

# İki yöntem de listeyi DOLDURUYOR ama farklı DURDURMA mantığı kullanıyor:
# birincisi "tam 5 kere" (sayaç), ikincisi "0 girilene kadar" (sentinel).


# --- SEN YAP ---
# Boş bir liste oluştur. while döngüsüyle kullanıcıdan TAM 4 tane isim al
# (input ile) ve her birini append() ile listeye ekle.
# Döngü bitince listenin tamamını ekrana yazdır.
# Kullanacağın metod: input(), append(), print()
# Kullanacağın operatör: <, +=
