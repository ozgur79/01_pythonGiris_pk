"""
pk250 çözümü — while(True) + if-else pratik
"""

while True:
    not_puan = int(input("Notunuzu girin (çıkmak için -1 girin): "))
    if not_puan == -1:
        break
    if not_puan >= 50:
        print("Geçti")
    else:
        print("Kaldı")
