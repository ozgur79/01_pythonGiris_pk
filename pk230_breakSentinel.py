"""
pk230 — break, sentinel (durdurucu değer)
Önkoşul: pk220 (sayaçla biriktirme)
Kazanım: break ile döngüyü erken sonlandırabilir, "belirli değer girilene kadar"
kalıbını kurabilir.
kaynak: arsiv/01_9B_2026/103whileBreak.py, arsiv/01_9B_2026/ss01_negatifPozitifSıfır.py
"""

# --- KAVRAM ---

# "while True:" yazarsan koşul HER ZAMAN True'dur, döngü KENDİLİĞİNDEN bitmez —
# SONSUZ döngü olur. Bu tehlikeli görünür ama aslında çok kullanışlıdır: döngüden
# çıkış kararını while'ın koşuluna değil, İÇERİDEKİ bir if'e bırakabilirsin.
# break, o if'in içinde "artık dur" demenin yoludur — çalıştığı anda döngü BİTER.

while True:
    sayi = int(input("Bir sayı girin (çıkmak için 5 girin): "))
    if sayi == 5:
        print("5 girildi, döngüden çıkılıyor.")
        break   # döngü burada anında biter, while'ın koşuluna hiç bakılmaz
    else:
        print("5 değil, devam ediliyor.")

print("Program bitti.")

# Bu kalıba "sentinel" (durdurucu/nöbetçi değer) denir: belirli bir değer
# (yukarıda 5) girilene kadar döngü devam eder, o değer görülünce break ile çıkılır.
# Aşağıda başka bir sentinel örneği — burada "0" girilene kadar analiz devam ediyor:

while True:
    sayi = int(input("Analiz edilecek sayıyı girin (çıkmak için 0 girin): "))
    if sayi > 0:
        print("pozitif")
    elif sayi < 0:
        print("negatif")
    else:
        print("Programdan çıkıldı")
        break


# --- SEN YAP ---
# while True ile sonsuz bir döngü kur. Kullanıcıdan sürekli bir kelime al.
# Kullanıcı "dur" yazana kadar (sentinel değer "dur") her girilen kelimeyi
# aynen ekrana yazdır ("Yazdığın: <kelime>" formatında).
# "dur" girildiğinde "Görüşürüz!" yazdır ve break ile döngüden çık.
# Kullanacağın metod: input(), print()
# Kullanacağın operatör: ==
