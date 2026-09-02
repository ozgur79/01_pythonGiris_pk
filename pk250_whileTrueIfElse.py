"""
pk250 — while(True) + if-else pratik
Önkoşul: pk240 (continue)
Kazanım: Sonsuz döngüyü koşullu break ile güvenli kapatabilir.
kaynak: arsiv/01_9B_2026/052enBoySoru.py (arşivde break mantığı bir yorum satırında
kalmış, program hiç bitmeyecek şekildeydi — bu script tamamlanmış hali)
"""

# --- KAVRAM ---

# pk230/pk240'ta break ve continue'yu tek tek gördük. Şimdi ikisini gerçek bir
# problemde birleştiriyoruz: kullanıcı en/boy bilgisi girip kare mi dikdörtgen
# mi olduğunu öğrenecek, 0 girene kadar bu devam edecek.

en = int(input("Eni girin (çıkmak için 0 girin): "))
boy = int(input("Boyu girin (çıkmak için 0 girin): "))

while True:
    if en == 0 or boy == 0:
        break  # sentinel: en ya da boy 0 girilirse döngüden hemen çık

    if en == boy:
        print("Kare")
    else:
        print("Dikdörtgen")

    en = int(input("Eni girin (çıkmak için 0 girin): "))
    boy = int(input("Boyu girin (çıkmak için 0 girin): "))

print("Programdan çıkıldı")

# Dikkat: break kontrolünü EN BAŞA koyduk (input'lardan hemen sonra), böylece
# 0 girildiğinde "Kare"/"Dikdörtgen" hesaplamasına hiç girmeden direkt çıkıyoruz.
# Kontrolü sona koysaydık da çalışırdı ama bir tur fazladan (gereksiz) iş yapardı.


# --- SEN YAP ---
# Kullanıcıdan sürekli bir not (0-100) al (while True ile).
# Kullanıcı -1 girene kadar devam et (-1 sentinel değeri, break ile çık).
# Her girilen not için: not >= 50 ise "Geçti", değilse "Kaldı" yazdır.
# Kullanacağın metod: input(), int(), print()
# Kullanacağın operatör: ==, >=
