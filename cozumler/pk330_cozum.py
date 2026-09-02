"""
pk330 çözümü — for'un sınırı: ne zaman while kullanılır
"""

# 1) n baştan biliniyor -> for kullanılır
n = int(input("Kaç yıldız istersin: "))
for i in range(n):
    print("*", end=" ")
print()

# 2) kaç kelime gireceği belli değil -> while kullanılır
while True:
    kelime = input("Bir kelime yaz (bitirmek için 'bitti' yaz): ")
    if kelime == "bitti":
        break
    print(kelime)
