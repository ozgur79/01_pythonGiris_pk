"""
pk510 — len(), find()
Önkoşul: pk470 (400 ünitesinin tamamı: liste)
Kazanım: Bir string'in uzunluğunu bulabilir, içinde geçen bir alt metnin
konumunu bulabilir.
kaynak: arsiv/01_9B_2026/305farkliMetodlar.py (len, find kısmı)
"""

# --- KAVRAM ---

metin = "Python programlama çok eğlenceli"

# len(): bir string'in KAÇ KARAKTERDEN oluştuğunu söyler (boşluklar da sayılır)
uzunluk = len(metin)
print("Metnin uzunluğu:", uzunluk)

# find(): aradığın alt metin, string İÇİNDE HANGİ INDEX'TE başlıyor, onu bulur
konum = metin.find("programlama")
print("'programlama' kelimesi, metinde index", konum, "'te başlıyor")

# Bulunamazsa find() -1 döndürür (hata VERMEZ, sadece -1 der)
konum2 = metin.find("java")
print("'java' kelimesinin konumu:", konum2)   # -1, çünkü metinde yok

# Not: len() sadece string'lerde değil, listelerde de çalışır (pk410'u hatırla,
# listenin eleman sayısını bulmak için de len(liste) kullanılabilir).
liste = [10, 20, 30]
print("Listenin eleman sayısı:", len(liste))


# --- SEN YAP ---
# Kullanıcıdan bir cümle al (input ile).
# Şunları ekrana yazdır:
#   1. Cümlenin uzunluğu (len ile)
#   2. Cümle içinde "python" kelimesinin geçtiği konum (find ile) -- yoksa -1 çıkacak, normal
# Kullanacağın metod: input(), len(), find(), print()
