"""
pk750 çözümü — Basit uygulama: sözlük/rehber
"""

sozluk = {}

while True:
    ingilizce = input("İngilizce kelime (bitirmek için 'bitir' yazın): ")
    if ingilizce == "bitir":
        break
    turkce = input("Türkçe karşılığı: ")
    sozluk[ingilizce] = turkce

for ingilizce in sozluk:
    print(ingilizce + " = " + sozluk[ingilizce])
