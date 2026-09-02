"""
pk620 — Tek parametreli fonksiyon, pratik
Önkoşul: pk610 (fonksiyon tanımı, parametre, return)
Kazanım: Gerçek bir problemi (daire alanı) fonksiyon olarak yazabilir.
kaynak: arsiv/01_9B_2026/501fonksiyon01.py (arşivde üs alma `r**2` kullanılmıştı,
üs alma hiç öğretilmediği için `r*r` ile değiştirildi)
"""

# --- KAVRAM ---

# pk610'daki topla(a,b) iki parametre alıyordu. Bu pratikte TEK parametreli
# gerçek bir problem çözeceğiz: yarıçapı verilen dairenin alanını hesaplama.
# Alan formülü: pi * yarıçap * yarıçap

def daire_alani_hesapla(yaricap):
    pi = 3.14
    alan = pi * yaricap * yaricap
    print("Daire alanı:", alan)

yari_cap = int(input("Yarıçapı girin: "))
daire_alani_hesapla(yari_cap)

# Bu fonksiyon return KULLANMIYOR -- sonucu direkt kendi içinde print() ile
# yazdırıyor. Bu da geçerli bir yaklaşım: bazı fonksiyonlar bir değer
# HESAPLAYIP GERİ VERİR (return), bazıları bir İŞ YAPAR (burada: ekrana yazma)
# ve hiçbir şey döndürmez.


# --- SEN YAP ---
# "kare_cevresi_hesapla" adında, tek parametre alan (kenar) bir fonksiyon
# tanımla. Fonksiyon, karenin çevresini (kenar * 4) hesaplayıp EKRANA
# YAZDIRSIN (yukarıdaki örnek gibi, return kullanma).
# Kullanıcıdan bir kenar uzunluğu al ve fonksiyonu çağır.
# Kullanacağın metod: def, input(), int(), print()
# Kullanacağın operatör: *
