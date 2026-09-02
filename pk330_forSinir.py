"""
pk330 — for'un sınırı: ne zaman while kullanılır
Önkoşul: pk320 (for ile biriktirme), pk230 (break, sentinel)
Kazanım: "Kaç kez tekrarlanacağı belliyse for, belli değilse while" ayrımını yapıp
aynı problemi doğru araçla çözebilir.
kaynak: YENİ — arsiv/01_9B_2026/150forTopluSorular_Arsivle.py'nin ss5 kısmındaki
`for _ in iter(int, 1):` kalıbının karşı-örnek olarak kullanılması
"""

# --- KAVRAM ---

# KURAL: Döngünün KAÇ KEZ döneceğini BAŞLAMADAN ÖNCE biliyorsan (bir sayı, bir
# aralık, bir liste boyutu) -> for kullan. Kaç kez döneceğini BİLMİYORSAN
# (kullanıcı "dur" diyene kadar, sıfır girilene kadar gibi) -> while kullan.
# Bu ders o ayrımı netleştiriyor.

# --- for NE ZAMAN doğru araç: sınır BAŞTAN belli ---
for i in range(1, 6):   # tam olarak 5 kez döneceğini BAŞLAMADAN biliyoruz
    print("Tur:", i)

# --- for NE ZAMAN YANLIŞ araç: sınır belli DEĞİL ---
# "Kullanıcı 0 girene kadar sayıları topla" problemini ele alalım. Kaç kez
# döneceğimizi ÖNCEDEN bilmiyoruz -- kullanıcıya bağlı. Arşivde bu tür
# durumlar için şöyle bir kalıp denenmiş (BU KODU ÇALIŞTIRMIYORUZ, sadece
# gösteriyoruz, yorum satırında bırakıldı):
#
#   toplam = 0
#   for _ in iter(int, 1):   # <-- KAFA KARIŞTIRICI, seviye üstü bir numara
#       sayi = int(input("Bir sayı girin: "))
#       if sayi == 0:
#           break
#       toplam += sayi
#
# Bu kod ÇALIŞIR ama iter(int, 1) çok az kişinin bildiği, okurken "bu ne
# demek?" dedirten bir numaradır -- for'u ZORLAYARAK sonsuz döngü gibi
# kullanmaktır. for'un doğal işi bu değil. Doğrusu şu (pk280'de zaten
# gördüğün kalıp):

toplam = 0
while True:
    sayi = int(input("Bir sayı girin (bitirmek için 0 girin): "))
    if sayi == 0:
        break
    toplam += sayi
print("Girilen sayıların toplamı:", toplam)

# while True + break, "ne zaman duracağını BİLMİYORUM" durumları için DOĞAL
# araçtır. for'u böyle bir duruma zorlamak yerine, doğru aracı (while) seç.


# --- SEN YAP ---
# İki ayrı program parçası yaz:
#   1. Kullanıcıdan bir sayı al (n). n TANE yıldız (*) yan yana yazdır.
#      (n baştan biliniyor -- hangi döngüyü kullanmalısın?)
#   2. Kullanıcıdan sürekli kelime al, kullanıcı "bitti" yazana kadar devam et,
#      her kelimeyi ekrana yazdır. (Kaç kelime gireceği BELLİ DEĞİL -- hangi
#      döngüyü kullanmalısın?)
# Her ikisinin de üstüne, hangi döngüyü neden seçtiğini bir yorum satırıyla açıkla.
# Kullanacağın metod: input(), print(), range()
