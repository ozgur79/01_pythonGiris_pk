"""
pk050 — String tekrar (*) gözlemi
Önkoşul: pk045 (hata mesajı okuma)
Kazanım: String ile int'in * davranış farkını gözlemler.
kaynak: arsiv/01_9B_2026/004intString.py (string tekrar kısmı)
"""

# --- KAVRAM ---

# Sayılarda * çarpma yapar: 5 * 4 = 20
print(5 * 4)

# String'lerde ise * TEKRAR yapar — çarpma değil.
s1 = input("Klavyeden bir kelime gir: ")
print(s1 * 4)  # kelimeyi 4 kere yan yana yazar, "çarpmaz"

# Aradaki fark, tipten kaynaklanıyor. int(s1) ile sayıya çevirirsek davranış değişir:
sayi = int(input("Klavyeden bir sayı gir: "))
print(sayi * 4)  # bu sefer gerçekten çarpıyor

# Özetle: aynı * işareti, string'de "tekrar", int'te "çarpma" anlamına gelir.
# Python bunu değişkenin TİPİNE bakarak kendisi ayırt eder.


# --- SEN YAP ---
# Kullanıcıdan bir isim (string) al ve ekrana o ismi 3 kere yan yana yazdır (string * 3).
# Ardından kullanıcıdan bir sayı al ve o sayının 3 katını hesaplayıp yazdır (int * 3).
# İki çıktı arasındaki farkı bir yorum satırı olarak scriptin en altına kendi
# cümlenle açıkla.
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: *
