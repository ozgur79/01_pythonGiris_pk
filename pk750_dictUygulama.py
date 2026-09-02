"""
pk750 — Basit uygulama: sözlük/rehber
Önkoşul: pk740 (for ile dict gezme), pk230 (while True + break, sentinel)
Kazanım: dict ile küçük bir sözlük veya telefon rehberi uygulaması yazabilir.
kaynak: YENİ
"""

# --- KAVRAM ---
# Bu ders yeni bir yapı öğretmiyor -- pk710-pk740'ta gördüğün her şeyi
# (oluşturma, ekleme, erişim, gezme) küçük bir programda birleştiriyoruz.

rehber = {}   # boş dict ile başla (boş liste = [] gibi, boş dict = {})

rehber["Ali"] = "0555 111 11 11"
rehber["Veli"] = "0555 222 22 22"
rehber["Ayşe"] = "0555 333 33 33"

print("--- Rehberdeki herkes ---")
for isim in rehber:
    print(isim, ":", rehber[isim])

print("--- Arama ---")
aranan = input("Kimin numarasını arıyorsun? ")
if aranan in rehber:
    print(aranan, "'in numarası:", rehber[aranan])
else:
    print(aranan, "rehberde kayıtlı değil.")


# --- SEN YAP ---
# Boş bir "sozluk" dict'i oluştur (İngilizce-Türkçe kelime sözlüğü gibi
# düşün, örn. "apple" -> "elma").
# while True + break kullanarak (sentinel: "bitir" yazılınca döngü dursun):
#   - kullanıcıdan bir İngilizce kelime al
#   - kullanıcıdan o kelimenin Türkçe karşılığını al
#   - ikisini sozluk'a ekle (sozluk[ingilizce] = turkce)
# Döngü bitince (kullanıcı "bitir" yazınca), sozluk'un TAMAMINI for ile gez
# ve her çifti "<ingilizce> = <turkce>" formatında yazdır.
# Kullanacağın metod: input(), print()
# Kullanacağın operatör: ==
