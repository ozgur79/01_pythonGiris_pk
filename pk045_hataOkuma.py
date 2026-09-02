"""
pk045 — Hata mesajı okuma
Önkoşul: pk040 (int() dönüşümü)
Kazanım: Python'ın verdiği hata mesajını okuyup hatanın türünü ve satırını bulabilir
(NameError, TypeError, ValueError, traceback'in son satırı; SyntaxError kısaca).
kaynak: YENİ — pk040'ta int() unutulup ilk TypeError/ValueError alınacağı an; hata
acıyı çektiği yerde öğretiliyor.
"""

# --- KAVRAM ---

# Kod hata verdiğinde Python paniklemene gerek olmayan, aslında YARDIMCI bir metin
# (traceback) yazdırır. Bu ders o metni okumayı öğretiyor.
#
# KURAL: Traceback'in EN ALT satırı asıl mesajdır. Üstündeki satırlar sadece
# hatanın nerede olduğunu gösteren "iz" (yol haritası). Önce en alta bak.

# --- 1) NameError: tanımlanmamış bir değişkeni kullanmaya çalışmak ---
# Aşağıdaki satırı çalıştırsaydık (yorumda bırakıldı, çünkü çalıştırırsak program çöker):
#   print(sayi)
# gerçek çıktı şu olurdu (bunu test ederek aldım):
#
#   Traceback (most recent call last):
#     File "...", line 1, in <module>
#       print(sayi)
#             ^^^^
#   NameError: name 'sayi' is not defined
#
# Okuma: en alt satır "NameError: name 'sayi' is not defined" diyor.
# Çeviri: "sayi" adında bir değişken hiç tanımlanmamış. Muhtemelen yazım hatası
# ya da o değişkeni atamayı unutmuşsundur.

# --- 2) TypeError: uyumsuz tiplerde işlem yapmaya çalışmak ---
# Aşağıdaki satırı çalıştırsaydık:
#   sonuc = "yas: " + 15
# gerçek çıktı şu olurdu:
#
#   Traceback (most recent call last):
#     File "...", line 1, in <module>
#       sonuc = 'yas: ' + 15
#   TypeError: can only concatenate str (not "int") to str
#
# Okuma: "can only concatenate str (not "int") to str" diyor.
# Çeviri: string'i ancak string ile birleştirebilirsin, int (15) ile değil.
# Çözüm: 15 yerine tırnak içine alınmış hali "15" yazılsaydı (yani sayı değil,
# string olsaydı), string+string olur ve hata olmazdı.

# --- 3) ValueError: dönüştürülemeyecek bir veriyi dönüştürmeye çalışmak ---
# Aşağıdaki satırı çalıştırsaydık (pk040'ta tam burada takılınır):
#   int("abc")
# gerçek çıktı şu olurdu:
#
#   Traceback (most recent call last):
#     File "...", line 1, in <module>
#       int('abc')
#   ValueError: invalid literal for int() with base 10: 'abc'
#
# Okuma: "invalid literal for int() with base 10: 'abc'" diyor.
# Çeviri: "abc" bir sayı değil, int()'e çeviremezsin.
# Bu, kullanıcı input()'a sayı yerine yazı girdiğinde SIK karşılaşacağın hatadır.

# --- 4) SyntaxError: Python'ın dilbilgisi kurallarına uymamak (kısaca) ---
# Örnek: parantezi kapatmayı unutmak, iki nokta üst üste (:) koymayı unutmak.
# SyntaxError diğer üçünden farklıdır: program ÇALIŞMAYA BİLE BAŞLAMAZ,
# çünkü Python kodu önce okur, sonra çalıştırır. Okurken bozuk bulursa hiç başlamaz.
# (Girinti hatası olan IndentationError da bir SyntaxError türüdür — onu pk110'da,
# if öğretilirken tekrar göreceksin.)

# --- SEN YAP ---
# Programı çalıştırdığında en sonda GERÇEK bir hata alacaksın (bu kasıtlı, script
# kasıtlı olarak çöküyor — bunu şimdiden biliyorsun, aşağı okumaya devam et).
# Çıkan traceback'in EN ALT satırını oku ve şu soruları kağıda/deftere cevapla:
#   1. Hatanın türü ne (hangi kelime ":"den önce yazıyor)?
#   2. Hata hangi satırda oluştu?
#   3. Bu hatayı düzeltmek için kodu nasıl değiştirirdin?


# --- Şimdi CANLI bir hata: bu satır kasıtlı olarak çalıştırılıyor ---
# (Yukarıdaki SEN YAP sorularını zaten okudun, şimdi çalıştırıp cevapla.)
print("Şimdi gerçek bir ValueError göreceksin, aşağıdaki satır kasıtlı olarak hatalı:")
sayi = int("dört")  # "dört" bir rakam değil, int() bunu çeviremez
