"""
pk420 — for ile liste üzerinde gezinme
Önkoşul: pk410 (liste nedir, oluşturma, index), pk310 (range() temelleri)
Kazanım: for eleman in liste ile bir listenin elemanlarını index kullanmadan gezebilir.
kaynak: arsiv/01_9B_2026/185listeDizi1.py
"""

# --- KAVRAM ---

# pk310/pk340'ta for'u hep range() ile kullandık: for i in range(...) demek,
# "range()'in ürettiği SAYILAR üzerinde gez" demekti. AYNI for yapısını,
# range() yerine DOĞRUDAN bir liste vererek de kullanabiliriz — bu sefer
# ürettiği sayılar üzerinde değil, listenin KENDİ ELEMANLARI üzerinde gezer.

liste = [1, 2, 3, 4, 5]

# --- Yöntem 1 (pk310'dan bildiğin): range ile index üzerinden gezmek ---
for i in range(5):
    print(liste[i])   # i sırayla 0,1,2,3,4 olur, liste[i] ile elemana ULAŞIRIZ

print("---")

# --- Yöntem 2 (bu dersin konusu): doğrudan liste üzerinde gezmek ---
for eleman in liste:
    print(eleman)      # "eleman" doğrudan listenin KENDİSİNİ tutar, index'e hiç gerek yok

# İki yöntem de AYNI ÇIKTIYI verir. Yöntem 2 daha kısa ve daha okunaklı --
# index'i hiç bilmen/hesaplaman gerekmiyor, Python listeyi baştan sona
# senin için geziyor. "eleman" adı senin seçimin, istediğin ismi verebilirsin.

for sehir in ["Sivas", "Ankara", "İzmir"]:
    print(sehir, "güzel bir şehir")


# --- SEN YAP ---
# Kendi seçtiğin 5 sayıdan oluşan bir liste oluştur.
# for eleman in liste kalıbıyla (index KULLANMADAN) listenin her elemanının
# KARESİNİ hesaplayıp ekrana yazdır.
# Kullanacağın metod: print()
# Kullanacağın operatör: *
