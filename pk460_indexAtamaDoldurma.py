"""
pk460 — Index atamasıyla liste doldurma
Önkoşul: pk410 (liste nedir, oluşturma, index), pk440 (while ile liste doldurma,
append()'in öğretildiği yer -- burada CONTRAST için referans veriliyor)
Kazanım: [0]*n ile boş liste oluşturup index ataması yapabilir (append'siz yöntem).
kaynak: arsiv/01_9B_2026/genelTekrar0_bosDizi.py
"""

# --- KAVRAM ---

# Liste, * ile TEKRARLANABİLİR (bir string'i * ile tekrar ettiğin gibi):
print([0] * 5)   # [0] elemanlı listeyi 5 kere tekrarlar -> [0, 0, 0, 0, 0]

# Bu, "N elemanlı, hepsi aynı değerde bir liste" oluşturmanın hızlı bir yolu.
# pk440/pk450'de append() ile listeyi SONUNA EKLEYEREK büyütmüştük. Şimdi
# FARKLI bir yöntem: listeyi baştan İSTENEN BOYUTTA oluşturup, sonra
# elemanları index ile TEK TEK DEĞİŞTİRİYORUZ (append kullanmadan).

liste = [0] * 5   # 5 elemanlı, hepsi 0 olan bir liste
sayac = 0
while sayac < 5:
    liste[sayac] = sayac * 10   # var olan elemanın ÜZERİNE YAZIYORUZ (append DEĞİL)
    sayac += 1
print("Doldurulan liste:", liste)

# Fark: append() listeyi BÜYÜTÜR (boştan başlayıp uzar). liste[i]=deger ise
# ZATEN VAR OLAN bir index'in değerini DEĞİŞTİRİR -- liste boyutu SABİT kalır.
# Bu yüzden [0]*5 ile ÖNCE 5 elemanlık yer açmak GEREKLİ, yoksa liste[sayac]=...
# satırı IndexError verirdi (pk045'i hatırla, henüz var olmayan bir index'e yazamazsın).


# --- SEN YAP ---
# [0] * 6 ile 6 elemanlı, hepsi 0 olan bir liste oluştur.
# while (ya da for, ikisi de olur) kullanarak, her index'e KENDİ index
# numarasının KARESİNİ yaz (index 0 -> 0, index 1 -> 1, index 2 -> 4,
# index 3 -> 9, index 4 -> 16, index 5 -> 25).
# Sonucu ekrana yazdır.
# Kullanacağın metod: print()
# Kullanacağın operatör: *, <
