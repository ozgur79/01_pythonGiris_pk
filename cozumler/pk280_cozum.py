"""
pk280 çözümü — Karma pratik
"""

sinir = int(input("Kaça kadar sayalım: "))
i = 0
while i < sinir:
    i += 1
    if i % 3 == 0:
        print("Fizz", end=" ")
    else:
        print(i, end=" ")
print()
