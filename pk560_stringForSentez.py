"""
pk560 — Pekiştirme: string + for sentezi
Önkoşul: pk540 (string indexleme ve dilimleme), pk320 (for ile biriktirme)
Kazanım: for ile string karakterlerini gezip sayma/tersten yazdırma/palindrome
gibi problemleri çözebilir.
kaynak: YENİ
"""

# --- KAVRAM ---
# Bu ders yeni bir yapı öğretmiyor -- pk420'de listeyi for ile gezmiştik
# (for eleman in liste), string'i de AYNI ŞEKİLDE for ile gezebiliriz --
# string, harflerden oluşan bir dizi olduğu için (pk540'ı hatırla).

kelime = input("Bir kelime girin: ")

# --- Harf sayma: belirli bir harften kaç tane var? ---
sayac = 0
for harf in kelime:
    if harf == "a":
        sayac += 1
print("'a' harfinden", sayac, "tane var")

# --- Tersten yazdırma: index'i geriye doğru gez (pk310'daki azalan range) ---
for i in range(len(kelime) - 1, -1, -1):
    print(kelime[i], end="")
print()

# --- Palindrome kontrolü: kelimeyi tersten yeniden oluştur, karşılaştır ---
ters = ""
for i in range(len(kelime) - 1, -1, -1):
    ters += kelime[i]   # pk220'deki += kısayolu, string birleştirmede de aynen çalışır

if kelime == ters:
    print("Bu kelime bir palindrome!")
else:
    print("Bu kelime palindrome değil.")


# --- SEN YAP ---
# Kullanıcıdan bir kelime al.
# for ile kelimenin harflerini gezerek:
#   1. Kaç tane SESLİ harf (a, e, i, ı, o, ö, u, ü) olduğunu say ve yazdır
#      (ipucu: her harf için "harf == 'a' or harf == 'e' or ..." ile kontrol et)
#   2. Kelimeyi BÜYÜK HARFE çevrilmiş olarak, harf harf, her harften sonra
#      bir tire (-) koyarak yazdır (örn. "kod" -> "K-O-D-")
# Kullanacağın metod: input(), upper(), print(end="")
# Kullanacağın operatör: or, +=
