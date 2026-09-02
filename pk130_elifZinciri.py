"""
pk130 — if-elif-else zinciri
Önkoşul: pk120 (if-else)
Kazanım: Çok koşullu (aralık bazlı) zincir kurabilir.
kaynak: arsiv/01_9B_2026/024puanNotChallengeCevap.py
"""

# --- KAVRAM ---

# if-else sadece İKİ yol sunuyordu. Ama gerçek hayatta genelde ikiden fazla
# durum vardır (kaldı/geçti/orta/iyi/pekiyi gibi). Bunun için elif ("else if"
# kısaltması) kullanılır. Zincir yukarıdan aşağıya, İLK True bulan koşulda durur,
# geri kalanına hiç bakmaz.

puan = int(input("Puanınızı girin: "))

if puan < 0:
    print("Geçersiz puan")
elif puan < 50:
    print("Kaldı")
elif puan < 55:
    print("Geçer")
elif puan < 70:
    print("Orta")
elif puan < 85:
    print("İyi")
elif puan < 101:
    print("Pekiyi")
else:
    print("Geçersiz puan")

print("Programdan çıkıldı... puan:", puan)

# Neden sıralama önemli: puan=40 girildiğinde Python önce "puan<0" mı diye bakar
# (Hayır), sonra "puan<50" mi diye bakar (Evet, 40<50) -> "Kaldı" yazdırır ve
# zincirin GERİSİNE HİÇ BAKMAZ. elif'leri ters sıralasaydık (önce puan<101,
# sonra puan<85 diye) sonuç YANLIŞ çıkardı çünkü zincir hep İLK uyanda durur.


# --- SEN YAP ---
# Kullanıcıdan bir yaş al.
# if-elif-else zinciriyle şu aralıklara göre mesaj yazdır:
#   yaş < 0            -> "Geçersiz yaş"
#   0 <= yaş < 13       -> "Çocuk"
#   13 <= yaş < 18      -> "Genç"
#   18 <= yaş < 65      -> "Yetişkin"
#   yaş >= 65           -> "Yaşlı"
# İpucu: pk130'daki gibi küçükten büyüğe sırayla < ile ilerle, ara sınırları
# ayrıca yazmana gerek yok (zincir zaten sırayla kontrol ediyor).
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: <, >=
