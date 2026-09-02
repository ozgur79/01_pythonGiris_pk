"""
pk660 çözümü — Varsayılan parametre değerleri
"""

def selam_ver(isim, dil="tr"):
    if dil == "tr":
        print("Merhaba", isim)
    elif dil == "en":
        print("Hello", isim)

selam_ver("Ali")
selam_ver("Veli", "en")
selam_ver("Ayşe", "tr")
