"""
pk280 — Karma pratik: faktöriyel, sentinel toplam, modulo desenleri
Önkoşul: pk270 (random modülü + while); kümülatif olarak pk220-pk270
Kazanım: Öğrenilen while kalıplarını karma bir problemde birleştirebilir.
kaynak: arsiv/01_9B_2026/106whileTopluSorular_Arsivle.py, arsiv/01_9B_2026/ssBOM.py
(mod-7 mantığı arşivde tutarsızdı, düzeltildi), arsiv/01_9B_2026/cevaplar2.1.py
(BOM kısmı, düzeltilmiş mantığın kaynağı)
"""

# --- KAVRAM ---

# --- 1) Faktöriyel: biriktirme kalıbı, bu sefer + değil * ile ---
# pk220'de toplam biriktirmiştik (toplam += sayac). Faktöriyelde AYNI kalıp
# ama çarparak biriktiriyoruz: 4! = 4*3*2*1
sayi = int(input("Faktöriyeli alınacak sayıyı girin: "))
sayac = 1
sonuc = 1
while sayac <= sayi:
    sonuc = sonuc * sayac   # her turda sonucu sayac ile çarpıyoruz (çarparak biriktirme)
    sayac += 1
print(sayi, "! =", sonuc)

# --- 2) Sentinel + toplam biriktirme birlikte ---
# pk230'da sentinel'i (0 girilene kadar) gördük, pk220'de toplam biriktirmeyi.
# Şimdi ikisini birleştiriyoruz: 0 girilene kadar sayıları topla.
toplam = 0
while True:
    sayi = int(input("Toplanacak sayıyı girin (bitirmek için 0 girin): "))
    if sayi == 0:
        break
    toplam += sayi
print("Girilen sayıların toplamı:", toplam)

# --- 3) % (mod) operatörü: bölümden KALAN ---
# % işareti, bir sayıyı diğerine böldüğünde KALANI verir.
print(7 % 2)   # 7'yi 2'ye bölersen 3 kalan 1 eder -> 1
print(10 % 5)  # 10'u 5'e bölersen 2 kalan 0 eder  -> 0
print(9 % 4)   # 9'u 4'e bölersen 2 kalan 1 eder   -> 1

# En önemli kullanımı: "sayi % n == 0" ise sayi, n'e TAM BÖLÜNÜYOR demektir
# (kalan sıfırsa tam bölünmüş olur). Örnek: 1'den 30'a kadar sayıları yazdır,
# ama 7'ye tam bölünen sayılar yerine "BOM" yaz.
i = 0
while i < 30:
    i += 1
    if i % 7 == 0:
        print("BOM", end=" ")
    else:
        print(i, end=" ")
print()


# --- SEN YAP ---
# 1'den kullanıcının girdiği bir sayıya kadar (dahil) olan sayıları while ile
# ekrana yazdır, ama 3'e tam bölünen sayılar yerine "Fizz" yazdır.
# Örnek çıktı (kullanıcı 9 girerse): 1 2 Fizz 4 5 Fizz 7 8 Fizz
# Kullanacağın metod: input(), int(), print(end=" ")
# Kullanacağın operatör: %, ==, <=
