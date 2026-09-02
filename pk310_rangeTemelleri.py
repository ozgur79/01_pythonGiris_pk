"""
pk310 — range() temelleri
Önkoşul: pk280 (200 ünitesinin tamamı: while)
Kazanım: range(n), range(a,b), range(a,b,adım) ile artan/azalan döngü kurabilir.
kaynak: arsiv/01_9B_2026/150forTopluSorular_Arsivle.py (ss1, ss2 kısmı)
"""

# --- KAVRAM ---

# while'da sayacı BİZ açıp BİZ artırıyorduk (sayac=1; while ...; sayac+=1).
# for, bunu SENİN YERİNE yapan farklı bir döngü türüdür. range() ile "kaç kez,
# nereden nereye" dersin, for da senin için sayar.

# --- range(n): 0'dan başlar, n'e KADAR gider (n DAHİL DEĞİL) ---
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4 yazar -- 5 YAZILMAZ

print("---")

# --- Aynı işi while ile yapsaydık (pk210'u hatırla) ---
i = 0
while i < 5:
    print(i)
    i += 1
# İki yöntem AYNI ÇIKTIYI verir. for, sayaç açma/artırma işini senin yerine yapıyor.

print("---")

# --- range(a, b): a'dan başlar, b'ye KADAR gider (b DAHİL DEĞİL) ---
for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5 yazar -- 6 YAZILMAZ

print("---")

# --- range(a, b, adim): a'dan b'ye, adim atlayarak gider ---
for i in range(10, 25, 5):
    print(i)   # 10, 15, 20 yazar -- 25 dahil değil

print("---")

# --- adim NEGATİF olursa, sayılar AZALARAK gider ---
for i in range(5, 0, -1):
    print(i)   # 5, 4, 3, 2, 1 yazar -- 0 dahil değil


# --- SEN YAP ---
# Üç ayrı for döngüsü yaz:
#   1. 0'dan 9'a kadar (9 dahil) tüm sayıları yazdır (range(n) kullan)
#   2. 100'den 130'a kadar (130 dahil), 10'ar 10'ar artarak yazdır
#   3. 20'den 1'e kadar (1 dahil), azalarak (tersten) yazdır
# Kullanacağın metod: range(), print()
