"""
pk410 — Liste nedir, oluşturma, index
Önkoşul: pk340 (300 ünitesinin tamamı: for, yalnızca range())
Kazanım: Liste oluşturabilir, pozitif/negatif index ile elemana erişebilir.
kaynak: arsiv/01_9B_2026/ssdiziTekrar_Arsivle.py (liste[0], liste[-1] kısmı) + YENİ (liste tanıtımı)
"""

# --- KAVRAM ---

# Liste, BİRDEN FAZLA değeri TEK BİR değişkende tutmanın yoludur. Köşeli
# parantez [ ] içine, virgülle ayırarak yazılır.
liste = [10, 20, 30, 40, 50]
print(liste)   # tüm listeyi tek seferde yazdırır

# Listenin her elemanına bir INDEX (sıra numarası) ile ulaşılır. Python'da
# index HER ZAMAN 0'dan başlar (1'den değil!).
print(liste[0])   # ilk eleman: 10
print(liste[1])   # ikinci eleman: 20
print(liste[4])   # beşinci (SON) eleman: 50

# NEGATİF index de vardır: SONDAN saymak için kullanılır. -1 her zaman SON
# elemanı gösterir, -2 sondan ikinciyi gösterir.
print(liste[-1])  # son eleman: 50 (liste[4] ile aynı sonucu verir)
print(liste[-2])  # sondan ikinci: 40

# Dikkat: liste[5] yazarsan IndexError alırsın (pk045'i hatırla) -- çünkü
# geçerli index'ler sadece 0, 1, 2, 3, 4'tür (5 eleman var, en büyük index 4).


# --- SEN YAP ---
# Kendi seçtiğin 6 şehir isminden oluşan bir liste oluştur (string listesi).
# Şunları ekrana yazdır:
#   1. Listenin tamamı
#   2. İlk şehir (index 0 ile)
#   3. Son şehir (negatif index ile)
#   4. Baştan üçüncü şehir (index 2 ile)
# Kullanacağın metod: print()
