"""
pk020 — Yorum satırı (tekli + çok satırlı) + string birleştirme + input
Önkoşul: pk010 (print, string literal)
Kazanım: # ile tekli, '''...'''/\"\"\"...\"\"\" ile çok satırlı yorum yazabilir (bundan
sonraki her scriptin tepesindeki docstring bloğunu tanır), input() ile veri alabilir,
+ ile string birleştirebilir.
kaynak: arsiv/01_9B_2026/002stringToplama1.py, arsiv/01_9B_2026/004intString.py (çok satırlı yorum kısmı)
"""

# --- KAVRAM ---

# Bu, "#" ile başlayan bir yorum satırıdır.
# Yorum satırları Python tarafından ÇALIŞTIRILMAZ, sadece insan okusun diye yazılır.
# Kodunu neden öyle yazdığını kendine ve başkasına hatırlatmak için kullanılır.

"""
Bu ise ÇOK SATIRLI bir yorumdur.
Üç tırnak (üç çift " ya da üç tek ') arasına yazılan her şey yorum sayılır,
kaç satır sürerse sürsün.
Bu dosyanın en tepesindeki açıklama bloğu (docstring) da aynı yapıyı kullanıyor —
bundan sonraki HER scriptin başında böyle bir blok göreceksin: dersin adı, önkoşulu,
kazanımı ve kaynağı orada yazılı olacak.
"""

# input() klavyeden veri alır. Aldığı veri HER ZAMAN string'dir (metin).
isim = input("Adını gir: ")

# + operatörü string'leri birleştirir (buna "string toplama" da denir).
mesaj = "Merhaba, " + isim + "!"
print(mesaj)

# Birden fazla input() ile alınan veriler de + ile birleştirilebilir.
sehir = input("Yaşadığın şehri gir: ")
print(isim + " " + sehir + "'da yaşıyor.")


# --- SEN YAP ---
# Kullanıcıdan sırasıyla "okul" ve "sınıf" bilgisini input() ile al.
# Bu iki bilgiyi + ile birleştirip şu formatta tek bir cümle yazdır:
#   "<okul> okulunun <sınıf>. sınıf öğrencisisin."
# Kullanacağın metod: input(), print()
# Kullanacağın operatör: +
