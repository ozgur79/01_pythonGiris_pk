"""
pk260 — İç içe while, desen çizimi
Önkoşul: pk210 (while temel), pk150 (iç içe if)
Kazanım: İki sayaçlı iç içe döngüyle satır/sütun deseni çizebilir.
kaynak: arsiv/01_9B_2026/114stringKare.py, arsiv/01_9B_2026/115stringUcgen.py,
arsiv/01_9B_2026/ss04.py, arsiv/01_9B_2026/ss05.py, arsiv/01_9B_2026/ss06.py
"""

# --- KAVRAM ---

# pk150'de iç içe if görmüştük: dıştaki koşul sağlanınca içtekine giriliyordu.
# İç içe while de aynı fikir, sadece döngü hâli: dıştaki while'ın HER TURUNDA,
# içteki while BAŞTAN SONA tamamen çalışıyor, sonra dıştaki bir sonraki tura geçiyor.

# Bir while'ın İÇİNE başka bir while koyabiliriz. DIŞTAKİ while SATIRLARI,
# İÇTEKİ while ise her satırdaki SÜTUNLARI (karakterleri) sayar.

# --- Örnek 1: 5x5'lik kare (aynı boyutlu satır/sütun) ---
satir = 1
while satir <= 5:
    sutun = 1
    while sutun <= 5:
        print("*", end=" ")  # end=" " print()'in satır SONUNA \n yerine boşluk koymasını sağlar
        sutun = sutun + 1
    print()  # boş print(), sadece satırı bitirip alt satıra geçer
    satir = satir + 1

print("---")

# --- Örnek 2: üçgen (her satırda bir yıldız fazla) ---
satir = 1
while satir <= 5:
    sutun = 1
    while sutun <= satir:   # DİKKAT: sınır artık sabit 5 değil, "satir" — bu yüzden üçgen oluşuyor
        print("*", end=" ")
        sutun = sutun + 1
    print()
    satir = satir + 1

# print()'in end= parametresi burada ilk kez kullanıldı: normalde her print()
# otomatik olarak satır sonuna "yeni satıra geç" (\n) ekler. end=" " dersen,
# bunun yerine boşluk ekler, böylece yıldızlar aynı satırda yan yana kalır.

# Not: pk220'de "sayac += 1" ile "sayac = sayac + 1"in aynı şey olduğunu görmüştük.
# Aynı kısayol çıkarma için de var: "sayac -= 1" demek "sayac = sayac - 1" demektir.


# --- SEN YAP ---
# İç içe while kullanarak TERS üçgen çiz (ilk satırda 5 yıldız, azalarak 1'e insin):
# * * * * *
# * * * *
# * * *
# * *
# *
# İpucu: dıştaki sayaç 5'ten başlayıp azalsın (satir >= 1 oldukça devam etsin,
# her turda satir -= 1 yap), içteki while her seferinde 1'den satir'e kadar yıldız bassın.
# Kullanacağın metod: print(end=" ")
# Kullanacağın operatör: <=, >=, -=
