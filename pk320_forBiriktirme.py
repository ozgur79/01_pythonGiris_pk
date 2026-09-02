"""
pk320 — for ile biriktirme, faktöriyel
Önkoşul: pk310 (range() temelleri)
Kazanım: for içinde sayaç olmadan toplam/çarpım biriktirebilir.
kaynak: arsiv/01_9B_2026/150forTopluSorular_Arsivle.py (ss3, ss4 kısmı)
"""

# --- KAVRAM ---

# pk220'de while ile toplam biriktirmiştik, sayacı BİZ açıp artırıyorduk.
# for'da sayaç (range'in verdiği i) HAZIR geldiği için, sadece biriktirme
# satırını yazman yeterli.

toplam = 0
for i in range(1, 11):
    toplam += i   # pk220'deki kısayol, burada da aynen çalışır
print("1'den 10'a kadar toplam:", toplam)

# --- Faktöriyel: çarparak biriktirme ---
# pk280'de while ile faktöriyel hesaplamıştık (sonuc = sonuc * sayac).
# for ile aynı işlem, sayaç yönetimi olmadan:

sayi = int(input("Faktöriyeli alınacak sayıyı girin: "))
sonuc = 1
for i in range(1, sayi + 1):   # 1'den sayi'ye KADAR DEĞİL, sayi DAHİL olsun diye sayi+1 yazıyoruz
    sonuc *= i   # "sonuc *= i" demek "sonuc = sonuc * i" demektir (pk220'deki += kısayolunun çarpma hali)
print(sayi, "! =", sonuc)

# Dikkat: range(1, sayi+1) yazdık, range(1, sayi) DEĞİL. Çünkü range(a,b) b'yi
# DAHİL ETMEZ (pk310'u hatırla) — sayi'nin kendisini de çarpıma katmak için
# üst sınırı bir fazla vermemiz gerekiyor.


# --- SEN YAP ---
# Kullanıcıdan bir sayı al (n).
# for ve range() kullanarak 1'den n'e kadar (n DAHİL) olan sayıların KARELERİNİN
# TOPLAMINI hesapla (1*1 + 2*2 + 3*3 + ... + n*n).
# Sonucu ekrana yazdır.
# Kullanacağın metod: input(), int(), range(), print()
# Kullanacağın operatör: +=, *
