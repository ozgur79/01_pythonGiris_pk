"""
pk470 — Liste analiz sentezi: sayma, toplam, ortalama
Önkoşul: pk440 (while ile liste doldurma), pk450 (for ile liste doldurma)
Kazanım: Girilen verileri listede toplayıp sayma/toplam/ortalama analizi yapabilir.
kaynak: arsiv/01_9B_2026/genelTekrar01_diziWhile.py (cevaplar2.1.py'de benzer
bir soru var, referans)
"""

# --- KAVRAM ---
# Bu ders yeni bir yapı öğretmiyor -- 400 ünitesindeki her şeyi (liste doldurma,
# if, biriktirme) TEK bir problemde birleştiriyor.

# Amaç: 5 öğrencinin yaşını al, listede topla; kaç kişi 18'den küçük, kaç
# kişi 18 ve üzeri, ortalama yaş kaç -- hepsini hesapla.

yaslar = []
kucuk_sayisi = 0
buyuk_esit_sayisi = 0
toplam = 0

sayac = 0
while sayac < 5:   # TAM 5 kez döneceğimiz baştan belli -- sayaç yeterli
    yas = int(input("Öğrencinin yaşını girin: "))
    yaslar.append(yas)
    if yas < 18:
        kucuk_sayisi += 1
    else:
        buyuk_esit_sayisi += 1
    toplam += yas
    sayac += 1

ortalama = toplam / 5   # kaç kişi girdiğimizi ZATEN BİLİYORUZ (5), bölen sabit

print("Girilen yaşlar:", yaslar)
print("18'den küçük:", kucuk_sayisi, "kişi")
print("18 ve üzeri:", buyuk_esit_sayisi, "kişi")
print("Ortalama yaş:", ortalama)


# --- SEN YAP ---
# Kullanıcıdan TAM 4 tane sınav notu al (0-100 arası), her birini bir listeye
# ekle. Aynı anda:
#   - kaç not 50'nin altında (kaldı) say
#   - kaç not 50 ve üzeri (geçti) say
#   - notların toplamını biriktir
# Döngü bitince: listenin tamamını, kaldı/geçti sayılarını ve notların
# ortalamasını (toplam / 4) ekrana yazdır.
# Kullanacağın metod: input(), int(), append(), print()
# Kullanacağın operatör: <, +=, /
