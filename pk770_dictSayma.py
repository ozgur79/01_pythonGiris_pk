"""
pk770 — dict ile sayma/gruplama
Önkoşul: pk740 (for ile dict gezme), pk560 (string + for sentezi)
Kazanım: Kelime sayma gibi klasik problemi dict ile çözebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# pk560'ta "for harf in kelime" ile belirli BİR harfi sayıyorduk (== ile
# tek tek kontrol ederek). Ama TÜM harflerin sayısını AYNI ANDA tutmak
# istersen, her harf için ayrı bir değişken açman gerekirdi -- pratik değil.
# dict tam bunun için var: her harfi ANAHTAR, o harften kaç tane olduğunu
# DEĞER olarak tutabiliriz.

kelime = input("Bir kelime girin: ")
sayac = {}   # boş dict ile başlıyoruz

for harf in kelime:
    if harf in sayac:
        sayac[harf] += 1   # bu harfi daha önce gördük, sayacını 1 artır
    else:
        sayac[harf] = 1    # bu harfi İLK KEZ görüyoruz, sayacı 1'den başlat

print("Harf sayıları:", sayac)

# Sonucu okunaklı yazdırmak için for ile gezebiliriz (pk740'taki gibi):
for harf in sayac:
    print(harf, ":", sayac[harf], "kere")


# --- SEN YAP ---
# Kullanıcıdan boşluklu bir cümle al (örn. "elma armut elma kiraz").
# Cümledeki her KARAKTERİ (boşluklar dahil) sayan bir dict oluştur
# (yukarıdaki harf sayma kalıbının aynısı, kelime yerine cümle).
# Sonucu for ile gezip her karakter ve sayısını yazdır.
# Kullanacağın metod: input(), print()
# Kullanacağın operatör: in, +=
