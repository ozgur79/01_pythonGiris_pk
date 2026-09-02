"""
pk620 — Tek parametreli fonksiyon, pratik
Önkoşul: pk610 (fonksiyon tanımı, parametre, return)
Kazanım: Fonksiyonun değer döndürmek (return) yerine doğrudan iş yapabileceğini
(print) ayırt eder; tek parametreli bir problemi fonksiyon olarak kurar.
kaynak: arsiv/01_9B_2026/501fonksiyon01.py (arşivde üs alma `r**2` kullanılmıştı,
üs alma hiç öğretilmediği için `r*r` ile değiştirildi)
"""

# --- KAVRAM ---

# pk610'daki topla(a,b) ve karesini_al(sayi) HEP return kullanıyordu -- bir
# değer HESAPLAYIP GERİ VERİYORLARDI. Ama her fonksiyonun bir değer
# döndürmesi GEREKMEZ: bazı fonksiyonlar sadece bir İŞ YAPAR (ekrana yazmak
# gibi) ve hiçbir şey return etmez. Aşağıdaki fonksiyon tam bu türden --
# dairenin alanını HESAPLAR ama return ETMEZ, kendi içinde print() eder.

def daire_alani_hesapla(yaricap):
    pi = 3.14
    alan = pi * yaricap * yaricap
    print("Daire alanı:", alan)   # return YOK -- fonksiyon işi burada bitiriyor

yari_cap = int(input("Yarıçapı girin: "))
daire_alani_hesapla(yari_cap)

# Fark neden önemli: return'lü fonksiyonun sonucunu bir değişkende SAKLAYIP
# başka yerde KULLANABİLİRSİN (pk610'daki topla(3,5) gibi). return'süz
# fonksiyonun ise "sonucu" yoktur -- sadece çağrıldığı anda işini yapar.
# İkisi de geçerlidir, hangisini seçeceğin fonksiyonun AMACINA bağlıdır.


# --- SEN YAP ---
# "kare_cevresi_hesapla" adında, tek parametre alan (kenar) bir fonksiyon
# tanımla. Fonksiyon, karenin çevresini (kenar * 4) hesaplayıp EKRANA
# YAZDIRSIN (yukarıdaki örnek gibi, return kullanma).
# Kullanıcıdan bir kenar uzunluğu al ve fonksiyonu çağır.
# Kullanacağın metod: def, input(), int(), print()
# Kullanacağın operatör: *
