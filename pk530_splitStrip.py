"""
pk530 — split(), strip()
Önkoşul: pk510 (len(), find()), pk410 (liste index)
Kazanım: String'i parçalara ayırabilir, baştaki/sondaki boşlukları temizleyebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

# strip(): string'in BAŞINDAKİ ve SONUNDAKİ boşlukları (varsa) siler.
# Ortadaki boşluklara DOKUNMAZ.
metin = "   Merhaba Dünya   "
print("[" + metin + "]")          # köşeli parantezler boşlukları GÖRÜNÜR yapmak için
print("[" + metin.strip() + "]")  # baştaki/sondaki boşluklar gitti

# Bu, kullanıcı input()'a istemeden fazladan boşluk yazdığında ("  evet " gibi)
# çok işe yarar -- karşılaştırma yapmadan önce strip() ile temizlenir.

# split(): string'i BOŞLUKLARDAN bölüp bir LİSTE döndürür.
cumle = "elma armut çilek"
kelimeler = cumle.split()
print(kelimeler)          # ['elma', 'armut', 'çilek']
print(kelimeler[0])       # liste olduğu için index ile erişilebilir (pk410'u hatırla)


# --- SEN YAP ---
# Kullanıcıdan boşluklu bir cümle al (örn. "kedi kopek kus").
# split() ile kelimelere ayır, kaç kelime girildiğini len() ile bul ve yazdır.
# Ayrıca kullanıcıdan başında/sonunda fazladan boşluk olan bir kelime al
# (örn. "   merhaba   " gibi -- kullanıcı bilerek boşluk eklesin), strip() ile
# temizleyip köşeli parantez içinde göster: "[temizlenmiş_hali]"
# Kullanacağın metod: input(), split(), strip(), len(), print()
