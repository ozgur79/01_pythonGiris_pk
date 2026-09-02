"""
pk450 — for ile liste doldurma
Önkoşul: pk430 (dilimleme), pk320 (for ile biriktirme)
Kazanım: for döngüsünde (range ile) append() ile n elemanlı liste doldurabilir.
kaynak: arsiv/01_9B_2026/186DiziyeKlavyedenVeriGirisiYAP.py
"""

# --- KAVRAM ---

# pk440'ta while ile "tam 5 kere" doldurmayı gördük (bir sayaç açıp elle
# artırarak). "Tam N kere" durumu, pk330'da öğrendiğin kurala göre TAM
# for'un işi -- kaç kez döneceğimiz baştan belli. append() aynen kullanılır,
# sadece sayaç yönetimini artık range() yapıyor.

liste = []
for i in range(5):
    sayi = int(input("Bir sayı girin: "))
    liste.append(sayi)   # pk440'ta öğrendiğin append(), burada da aynen çalışıyor
print("Girilen liste:", liste)

# "i" değişkenini burada hiç KULLANMADIK (sadece 5 kez dönmesi için vardı).
# Bu normaldir -- bazen for'un sayacına ihtiyacın olmaz, sadece "kaç kez
# döneceğini" belirlemek için range() yeterlidir.


# --- SEN YAP ---
# Boş bir liste oluştur. for ve range() kullanarak kullanıcıdan TAM 6 tane
# şehir ismi al (input ile) ve her birini append() ile listeye ekle.
# Döngü bitince listenin tamamını ekrana yazdır.
# Kullanacağın metod: input(), range(), append(), print()
