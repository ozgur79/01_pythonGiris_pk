"""
pk340 — İç içe for: çarpım tablosu
Önkoşul: pk310 (range() temelleri), pk260 (iç içe while)
Kazanım: İç içe while'dan (pk260) transfer ederek range ile iç içe döngü kurup
çarpım tablosu gibi klasik bir problemi çözebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# pk260'ta iç içe while ile desen çizmiştik: dıştaki döngünün her turunda,
# içteki döngü baştan sona çalışıyordu. İç içe for'da AYNI FİKİR geçerli,
# sadece sayaç yönetimini artık range() yapıyor.

# --- Önce pk260'taki kareyi for ile tekrar yapalım (transfer) ---
for satir in range(1, 6):
    for sutun in range(1, 6):
        print("*", end=" ")
    print()

print("---")

# --- Şimdi yeni bir klasik problem: 1'den 5'e kadar çarpım tablosu ---
for sayi in range(1, 6):
    for carpan in range(1, 11):
        sonuc = sayi * carpan
        print(sayi, "x", carpan, "=", sonuc)
    print()   # her sayının tablosu bitince bir boş satır bırak

# Dıştaki for "hangi sayının tablosunu yapıyoruz" (1, 2, 3, 4, 5), içteki for
# "o sayıyı 1'den 10'a kadar hangi carpanla çarpıyoruz" sorusuna cevap veriyor.
# Dıştaki HER TUR için, içteki TAM 10 TUR döner -- toplamda 5*10=50 satır yazılır.


# --- SEN YAP ---
# pk260'ta iç içe while ile TERS ÜÇGEN çizmiştin (ilk satırda 5 yıldız,
# azalarak 1'e insin). Şimdi AYNI deseni for ile çiz:
#
# * * * * *
# * * * *
# * * *
# * *
# *
#
# İpucu: KAVRAM'daki örneklerde içteki range()'in sınırları HEP SABİTTİ
# (range(1,6), range(1,11)). Burada içteki range()'in üst sınırı, dıştaki
# değişkene BAĞLI olmak zorunda (örn. dıştaki değişken "satir" ise,
# içteki range(1, satir + 1) gibi) -- yoksa üçgen değil kare çıkar.
# Kullanacağın metod: range(), print(end=" ")

