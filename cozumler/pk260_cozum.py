"""
pk260 çözümü — İç içe while, desen çizimi
"""

satir = 5
while satir >= 1:
    sutun = 1
    while sutun <= satir:
        print("*", end=" ")
        sutun += 1
    print()
    satir -= 1
