"""
pk550 — f-string ile biçimlendirme
Önkoşul: pk510 (len(), find()), pk020 (string birleştirme)
Kazanım: f"..." ile değişkenleri okunaklı biçimde string içine gömebilir.
kaynak: YENİ
"""

# --- KAVRAM ---

isim = "Ali"
yas = 15

# pk020'de değişkenleri + ile ya da print()'e virgülle vererek
# birleştiriyorduk. + ile string+int birleştirmek İSTERSEN (pk045'te bunun
# TypeError verdiğini görmüştük), önce int'i string'e çevirmen gerekir --
# bunun için str() kullanılır (int()'in TERSİ: sayıyı yazıya çevirir):
print(isim + " " + str(yas) + " yaşındadır.")
print(isim, yas, "yaşındadır.")   # virgülle bu sorun yoktu, ama araya
                                    # istediğin kelimeyi karıştırmak zordu

# f-string ile: string'in başına "f" koyup, süslü parantez { } içine
# DOĞRUDAN değişken yazabilirsin -- tip dönüştürmeye GEREK YOK, Python
# otomatik hallediyor:
print(f"{isim} {yas} yaşındadır.")

# İçine hesap da yazabilirsin, { } parantezinin içi ÇALIŞTIRILIR:
print(f"5 yıl sonra {isim}, {yas + 5} yaşında olacak.")

# f-string, özellikle çok değişkenli/uzun cümlelerde + ile birleştirmekten
# çok daha okunaklıdır -- artık tercih edeceğin yöntem bu olacak.


# --- SEN YAP ---
# Kullanıcıdan isim, şehir ve yaş bilgisi al (üç ayrı input, yaş int olsun).
# f-string kullanarak şu formatta TEK bir cümle yazdır:
#   "<isim>, <şehir>'de yaşıyor ve <yaş> yaşında."
# Kullanacağın metod: input(), int(), print()
