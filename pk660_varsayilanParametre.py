"""
pk660 — Varsayılan parametre değerleri
Önkoşul: pk610 (fonksiyon tanımı, parametre, return), pk620 (return'süz, iş
yapan fonksiyon -- ilk örnekteki selamla() bu türden), pk130 (if-elif-else
zinciri -- SEN YAP'ta kullanılıyor)
Kazanım: Parametreye varsayılan değer atayabilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# Bir parametreye, fonksiyon tanımlanırken "eğer çağıran taraf bu değeri
# VERMEZSE kullanılacak" bir VARSAYILAN DEĞER atayabilirsin.

def selamla(isim, mesaj="Merhaba"):
    print(mesaj, isim)

selamla("Ali")              # "mesaj" verilmedi -> varsayılan "Merhaba" kullanılır
selamla("Veli", "Selam")    # "mesaj" verildi -> "Selam" kullanılır, varsayılan GÖRMEZDEN GELİNİR

# Varsayılan değerli parametreler, fonksiyon tanımında EN SONA yazılır
# (varsayılansız parametrelerden sonra). Şöyle bir sıralama HATA verir:
#   def selamla(mesaj="Merhaba", isim): ...   -- YANLIŞ, varsayılansız parametre
#                                                varsayılanlıdan SONRA gelemez

# --- İkinci örnek: sayısal varsayılan değer ---
def ucret_hesapla(saat, saatlik_ucret=50):
    return saat * saatlik_ucret

print("Varsayılan ücretle:", ucret_hesapla(10))          # saatlik_ucret verilmedi -> 50 kullanılır
print("Özel ücretle:", ucret_hesapla(10, 75))              # saatlik_ucret verildi -> 75 kullanılır


# --- SEN YAP ---
# "selam_ver" adında bir fonksiyon tanımla: "isim" parametresi zorunlu olsun,
# "dil" parametresinin varsayılan değeri "tr" olsun.
# Fonksiyon, dil "tr" ise "Merhaba <isim>", dil "en" ise "Hello <isim>" yazdırsın
# (if-elif ile kontrol et).
# Fonksiyonu üç farklı şekilde çağır: sadece isimle, isim+dil="en" ile, ve
# isim+dil="tr" ile.
# Kullanacağın metod: def, print()
