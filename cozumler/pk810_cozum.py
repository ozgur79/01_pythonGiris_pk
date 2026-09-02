"""
pk810 çözümü — Dosyaya yazma, dosyadan okuma
"""

cumle = input("Bir cümle girin: ")

with open("notum.txt", "w", encoding="utf-8") as dosya:
    dosya.write(cumle)

with open("notum.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("Dosyanın içeriği:", icerik)
