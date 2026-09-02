"""
pk170 — Pekiştirme: and ile bağımsız pratik
Önkoşul: pk150 (and operatörü)
Kazanım: and operatörünü yeni bir problemde bağımsız kurabilir.
kaynak: arsiv/01_9B_2026/ss02.py (tema değiştirildi: orijinaldeki askerlik/cinsiyet
teması yerine yaş + kurs tamamlama koşulu kullanıldı)
"""

# --- KAVRAM ---
# Bu ders yeni bir şey öğretmiyor — pk150'de gördüğün and operatörünü FARKLI bir
# senaryoda tekrar görüyorsun. Aşağıdaki örnek, "iki koşulun ikisi de sağlanmalı"
# kalıbının bir başka kullanımı.

yas = int(input("Yaşınızı girin: "))
kurs_tamamlandi_mi = input("Sürücü kursunu tamamladınız mı? (evet/hayir): ")

if yas >= 18 and kurs_tamamlandi_mi == "evet":
    print("Ehliyet alabilir.")
else:
    print("Ehliyet alamaz.")

# Burada da and'in mantığı aynı: yaş koşulu VE kurs koşulu, İKİSİ BİRDEN True
# olmalı. Sadece yaşı tutup kursu tamamlamamış biri (ya da tam tersi) yine
# else'e düşer.


# --- SEN YAP ---
# Kullanıcıdan bir sınav notu (int) ve devamsızlık gün sayısı (int) al.
# Eğer not >= 50 VE devamsızlık <= 10 ise "Sınıfı geçti" yazdır.
# Değilse (else) "Sınıfı geçemedi" yazdır.
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: and, >=, <=
