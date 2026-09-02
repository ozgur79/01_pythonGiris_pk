"""
pk820 — Dosyayı satır satır okuma
Önkoşul: pk810 (dosyaya yazma, dosyadan okuma), pk410 (liste), pk420
(for eleman in liste), pk510 (len()), pk260 (end= parametresi)
Kazanım: readlines() ile dosyayı bir liste olarak alıp for ile satır satır
işleyebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# Önce birden çok satırlı bir dosya oluşturalım. pk020'deki üçlü tırnak
# (çok satırlı yazım) burada bir YORUM değil, GERÇEK BİR STRING DEĞERİ olarak
# kullanılıyor -- satır atlamaları string'in İÇİNE gerçekten kaydediliyor:

gunluk_metni = """Bugün Python öğrendim.
Yarın liste konusuna geçeceğim.
Sonra fonksiyonlara bakacağım."""

with open("gunluk.txt", "w", encoding="utf-8") as dosya:
    dosya.write(gunluk_metni)

# read() dosyanın TAMAMINI TEK BİR string olarak veriyordu (pk810'u hatırla).
# readlines() ise dosyayı SATIR SATIR bölüp bir LİSTE döndürür -- her liste
# elemanı bir satırdır (pk410'daki liste ile birebir aynı şekilde kullanılır):

with open("gunluk.txt", "r", encoding="utf-8") as dosya:
    satirlar = dosya.readlines()

print(satirlar)   # bir liste olduğunu görürsün: ['Bugün...\n', 'Yarın...\n', 'Sonra...']
print("Kaç satır var:", len(satirlar))

# Yukarıdaki çıktıda "\n" gördün -- bu, "yeni satıra geç" anlamına gelen özel
# bir karakter, dosyadaki HER satırın (sonuncusu hariç) SONUNDA gerçekten var.
# print() zaten kendiliğinden satır sonuna "yeni satıra geç" ekliyordu
# (pk010'dan beri) -- satır zaten kendi "\n"ini taşıdığı için, ikisi üst üste
# binmesin diye end="" kullanıyoruz (pk260'ı hatırla):

for satir in satirlar:
    print("->", satir, end="")
print()   # son satırın ardından temiz bir satır sonu için


# --- SEN YAP ---
# "alisveris.txt" adında bir dosyaya, üçlü tırnaklı çok satırlı bir string
# kullanarak 4 alışveriş kalemi yaz (her kalem kendi satırında, örn. "Ekmek",
# "Süt", "Yumurta", "Peynir").
# Dosyayı readlines() ile oku, for ile gez, her kalemi başına bir "- " (tire,
# boşluk) ekleyerek yazdır (örn. "- Ekmek").
# Kullanacağın metod: open(), write(), readlines(), print()
