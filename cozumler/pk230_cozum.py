"""
pk230 çözümü — break, sentinel
"""

while True:
    kelime = input("Bir kelime yaz (çıkmak için 'dur' yaz): ")
    if kelime == "dur":
        print("Görüşürüz!")
        break
    print("Yazdığın:", kelime)
