"""
pk610 — Fonksiyon tanımı, parametre, return
Önkoşul: pk560 (500 ünitesinin tamamı: string metodları), pk040 (int, aritmetik)
Kazanım: def ile fonksiyon tanımlayıp parametre alıp return ile sonuç döndürebilir.
kaynak: arsiv/01_9B_2026/500fonksiyon00.py
"""

# --- KAVRAM ---

# Şimdiye kadar kodumuz hep YUKARIDAN AŞAĞIYA, tek seferlik çalıştı. Fonksiyon,
# bir kod parçasını İSİMLENDİRİP paketleyip, istediğin kadar TEKRAR TEKRAR
# çağırabilmeni sağlar -- aynı işi her seferinde yeniden yazmadan.

def topla(a, b):
    # "a" ve "b" bu fonksiyonun PARAMETRELERİ -- fonksiyon çağrılırken
    # dışarıdan verilen değerleri tutan, sadece bu fonksiyonun içinde
    # geçerli olan değişkenler.
    return a + b   # return, fonksiyonun SONUCUNU çağıran yere geri gönderir

# Fonksiyonu ÇAĞIRMAK: parantez içine gerçek değerleri (argüman) yazarsın.
sonuc = topla(3, 5)   # a=3, b=5 olarak fonksiyona gönderilir
print("Toplam:", sonuc)

# Aynı fonksiyonu FARKLI değerlerle tekrar tekrar çağırabilirsin -- kodu
# yeniden yazmana gerek yok:
print("Bir başka toplam:", topla(10, 20))
print("Yine bir toplam:", topla(100, 1))

# --- İkinci örnek: tek parametreli fonksiyon ---
def karesini_al(sayi):
    return sayi * sayi

print("5'in karesi:", karesini_al(5))
print("8'in karesi:", karesini_al(8))

# Dikkat: return'den sonraki satırlar ÇALIŞMAZ -- fonksiyon return'e gelince
# ANINDA durur ve değeri geri gönderir.


# --- SEN YAP ---
# "carp" adında, iki parametre alan (a, b) bir fonksiyon tanımla.
# Fonksiyon, a ile b'nin çarpımını return etsin.
# Fonksiyonu üç farklı sayı çiftiyle çağırıp sonuçlarını print() ile yazdır.
# Kullanacağın metod: def, return, print()
# Kullanacağın operatör: *
