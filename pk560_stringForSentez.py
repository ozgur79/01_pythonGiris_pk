"""
pk560 — Pekiştirme: string + for sentezi
Önkoşul: pk540 (string indexleme ve dilimleme), pk320 (for ile biriktirme),
pk420 (for eleman in liste -- bu dersin temel dayanağı), pk520 (upper(),
SEN YAP'ta kullanılıyor)
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

# --- Tersten yazdırma + palindrome: TEK döngüde, index'e hiç gerek kalmadan ---
# Her yeni harfi, biriktirdiğimiz string'in SONUNA değil BAŞINA ekliyoruz --
# bu, harflerin sırasını kendiliğinden tersine çeviriyor.
ters = ""
for harf in kelime:
    ters = harf + ters   # her yeni harf BAŞA ekleniyor -> sıra tersine dönüyor

print("Tersten yazılışı:", ters)

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
