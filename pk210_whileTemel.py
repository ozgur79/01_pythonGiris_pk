"""
pk210 — while temel, girinti
Önkoşul: pk170 (100 ünitesinin tamamı: karar yapıları)
Kazanım: Koşul doğru olduğu sürece tekrar eden döngü yazabilir.
kaynak: arsiv/01_9B_2026/100while.py, arsiv/01_9B_2026/101whileGirinti.py
"""

# --- KAVRAM ---

# if, bir koşulu SADECE BİR KEZ kontrol ediyordu. while ise koşul True olduğu
# SÜRECE, aynı bloğu TEKRAR TEKRAR çalıştırır. Koşul False olunca döngü biter.

x = 1
while x < 6:
    print(x, ". tekrar")
    x = x + 1   # bu satır olmasaydı x hep 1 kalırdı, koşul HİÇ False olmazdı (sonsuz döngü)

print("while'dan çıkıldı, x artık:", x)

# Girinti burada da if'teki gibi çalışır: while'ın altındaki (girintili) satırlar
# HER TEKRARDA çalışır, girintisiz satır döngü BİTTİKTEN SONRA bir kez çalışır.

sayac = 1
while sayac < 11:
    print(sayac)              # while bloğuna AİT, her turda çalışır
    sayac = sayac + 1         # while bloğuna AİT, her turda çalışır
sayac = sayac + 1              # GİRİNTİ YOK: while bloğuna AİT DEĞİL, döngü bitince BİR KEZ çalışır
print("Döngü bitti, sayac:", sayac)


# --- SEN YAP ---
# 1'den 20'ye kadar olan sayıları (20 dahil) while ile ekrana yazdır.
# Her sayıyı ayrı satırda yazdır.
# Kullanacağın metod: print()
# Kullanacağın operatör: <= veya <
