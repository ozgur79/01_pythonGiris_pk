"""
pk240 — continue
Önkoşul: pk230 (break, sentinel)
Kazanım: continue ile döngünün kalan gövdesini atlayıp bir sonraki tura geçebilir.
kaynak: arsiv/01_9B_2026/104whileContinue.py
"""

# --- KAVRAM ---

# break döngüyü TAMAMEN bitiriyordu. continue ise farklı: döngüyü bitirmez,
# sadece O TURUN geri kalan satırlarını ATLAR ve while'ın başına (koşul
# kontrolüne) döner. Döngü devam eder.

while True:
    cevap = input("Devam etmek istiyor musunuz? (evet/hayir): ")

    if cevap == "evet":
        print("Devam ediliyor...")
        continue  # buradan sonraki satırlara (aşağıdaki print("Hey")) HİÇ UĞRAMADAN, döngü başına döner
    elif cevap == "hayir":
        print("Döngüden çıkılıyor.")
        break
    else:
        print("Geçersiz giriş. Lütfen 'evet' veya 'hayir' girin.")

    print("Hey")  # SADECE geçersiz giriş yapılınca çalışır:
                  # "evet" continue ile bu satırı atlar, "hayir" break ile döngüden çıkar

print("Hoscakal")

# Özet: break = döngüyü tamamen bitir. continue = bu turu bitir, döngüye devam et.


# --- SEN YAP ---
# while True ile sonsuz bir döngü kur. Kullanıcıdan sürekli bir sayı al.
# Eğer sayı negatifse (0'dan küçükse) "Negatif sayıları saymıyorum!" yazdır ve
# continue ile bir sonraki turu başlat (aşağıdaki satırlara inme).
# Negatif değilse sayının karesini hesaplayıp yazdır.
# Kullanıcı 0 girerse "Bitti" yazdır ve break ile döngüden çık.
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: <, ==, *
