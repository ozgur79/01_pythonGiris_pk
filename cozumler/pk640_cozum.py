"""
pk640 çözümü — Fonksiyon + if-elif-else sentezi
"""

def not_degerlendir(puan):
    if puan < 50:
        print("Kaldı")
    elif puan < 70:
        print("Orta")
    else:
        print("İyi")

not_degerlendir(30)
not_degerlendir(60)
not_degerlendir(90)
