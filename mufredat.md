# Müfredat — 9. Sınıf Python Giriş (pk)

Durum: **onaylandı**. Script üretimi (FAZ 2) başladı — ünite ünite ilerliyor, her ünite
bitince durup onay bekleniyor.
Kaynak: `D:\Atolye\Python\arsiv\01_9B_2026` (59 dosya, dokunulmadı, sadece okundu).

**Özet (ders düzeyi):** 57 ders — **46 çekirdek, 11 genişletme**. Bağlam: haftada 2 saat ×
~36 hafta ≈ 72 ders saati; bazı scriptler bir saatten uzun sürer, yani 57 dersin hepsi rahat
sığmayabilir.

**Özet (ünite düzeyi):** Ders bazındaki çekirdek/genişletme etiketi bir kör nokta taşıyor —
bir ünitenin dersleri birbirini önkoşul alıyorsa (ör. 700: pk710→720→730→740→750) o zincir
kendi içinde kapalı olduğu için hepsi "çekirdek" görünür, ama müfredatın dışarıdan o üniteye
bağımlılığı sıfır olabilir. Bu yüzden ünite düzeyinde ayrı bir öncelik var (aşağıda): 000-600
**çekirdek ünite** (bitmeden yıl tamamlanmış sayılmaz), 700 (dict) ve 800 (dosya) **genişletme
ünitesi** — sıkışırsa serpiştirilmiş ders değil, bütün ünite düşer.

İsimlendirme: `pk<üç basamak>_<isimKisaAdi>.py`. Yüzler basamağı = ünite. Numaralar 10'ar artar.
Boş numara bırakmak serbest.

**Öncelik etiketi nasıl belirlendi (ders düzeyi):** Mekanik kural — bir ders başka bir dersin
önkoşuluysa `çekirdek`, hiçbir dersin önkoşulu değilse (yaprak) `genişletme` **adayı**. Ama her
yaprak tek tek değerlendirildi; bazıları (pk160, pk330, pk520, pk550, pk650) yaprak olmasına
rağmen gerekçeyle `çekirdek`'e yükseltildi, gerisi `genişletme` kaldı ve her birine tek
cümlelik gerekçe yazıldı.

## Ünite planı

| Ünite | Konu | Öncelik (ünite düzeyi) |
|---|---|---|
| 000 | Temel (çıktı, yorum, input, veri tipi, dönüşüm, değişken, biriktirme, hata okuma) | çekirdek ünite |
| 100 | Karar yapıları (if, if-else, elif zinciri, and/or, iç içe if) | çekirdek ünite |
| 200 | while | çekirdek ünite |
| 300 | for — yalnızca `range()` | çekirdek ünite |
| 400 | liste — `for eleman in liste` burada öğretilir | çekirdek ünite |
| 500 | string metodları | çekirdek ünite |
| 600 | fonksiyon | çekirdek ünite |
| 700 | sözlük (dict) | **genişletme ünitesi** — bütün olarak düşebilir |
| 800 | dosya işlemleri (kapanış ünitesi) | **genişletme ünitesi** — bütün olarak düşebilir |

## Çözüm dosyaları politikası

`cozumler/` klasörü açılacak, repoda **public** kalacak. pk*.py scriptlerinin içindeki
"SEN YAP" bölümünde **asla** cevap olmayacak — cevaplar sadece `cozumler/pk<numara>_cozum.py`.

---

## 000 — Temel

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk010 | İlk program: print, string literal | `print()` ile ekrana metin yazdırabilir | — | çekirdek | 001merhaba.py |
| pk020 | Yorum satırı (tekli + çok satırlı) + string birleştirme + input | `#` ile tekli, `'''...'''`/`"""..."""` ile çok satırlı yorum yazabilir (bundan sonraki her scriptin tepesindeki docstring bloğunu tanır), `input()` ile veri alabilir, `+` ile string birleştirebilir | pk010 | çekirdek | 002stringToplama1.py, 004intString.py (çok satırlı yorum kısmı) |
| pk030 | Çoklu string birleştirme | Birden çok string değişkeni `+` ile anlamlı bir cümlede birleştirebilir | pk020 | genişletme — 020'deki string birleştirmenin çok değişkenli tekrarı, kavram zaten 020'de var | 002stringToplama2.py |
| pk040 | int() dönüşümü, sayısal toplama | `int(input())` ile sayısal veri alıp aritmetik işlem yapabilir | pk020 | çekirdek | 003intToplama.py |
| pk045 | Hata mesajı okuma | Python'ın verdiği hata mesajını okuyup hatanın **türünü ve satırını** bulabilir (`NameError`, `TypeError`, `ValueError`, traceback'in son satırı; `SyntaxError` kısaca) | pk040 | çekirdek | YENİ — pk040'ta `int()` unutulup ilk `TypeError`/`ValueError` alınacağı an; hata acıyı çektiği yerde öğretiliyor |
| pk050 | String tekrar (*) gözlemi | String ile int'in `*` davranış farkını gözlemler | pk045 | genişletme — sonraki hiçbir dersin kazanımı string çarpımına dayanmıyor; çok satırlı yorum pk020'ye taşındı çünkü her scriptin docstring'inde zaten görülüyor, atlanamaz | 004intString.py (string tekrar kısmı) |
| pk060 | Değişkende ara sonuç saklama | Değişkende hesap sonucunu saklayıp tekrar kullanabilir | pk040 | çekirdek | 010degiskenKaresi.py |
| pk070 | print() içinde değişken/string literal farkı | `print(isim)` ile `print("isim")` arasındaki farkı ayırt edebilir (yaygın başlangıç hatası) | pk060 | çekirdek | 011degiskenIsimYil.py |
| pk080 | Biriktirme (accumulator) girişi | Aynı değişkeni güncelleyerek çoklu girdiyi tek değişkende toplayabilir | pk070 | çekirdek | 013ucSayiIkiDegisken.py |
| pk090 | Pekiştirme: temel ünitesi karma | Ünitedeki tüm kalıpları (input, dönüşüm, birleştirme, biriktirme) bağımsız yazabilir | pk080 (kümülatif: pk010-080) | çekirdek | 014Soru.py, 015Soru.py |

**Kullanılmayan/duplicate:** 002string.....py (001 ile birebir aynı içerik).

---

## 100 — Karar yapıları

Arşivde tam 7 kaynak dosya var, ünite 7 dersten oluşuyor.

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk110 | if temel, girinti, karşılaştırma operatörleri | `>`,`<`,`>=`,`<=`,`==`,`!=` ile koşul yazabilir, girintinin blok belirlediğini bilir (girinti hatası — `IndentationError` — pk045'e geri bağlanır) | pk090 | çekirdek | 020ifEhliyet.py |
| pk120 | if-else | İki dallı karar yapısı kurabilir | pk110 | çekirdek | 021ifEhliyet.py |
| pk130 | if-elif-else zinciri | Çok koşullu (aralık bazlı) zincir kurabilir | pk120 | çekirdek | 024puanNotChallengeCevap.py |
| pk140 | if-elif pratik, farklı senaryo | elif zincirini farklı bir problemde (string karşılaştırmalı) tekrar kurabilir | pk130 | genişletme — 130'da öğretilen elif zincirinin tekrar pratiği, yeni kazanım eklemiyor | 032hesapMakinesiCevapBITMEDI.py* |
| pk150 | and operatörü + iç içe if karşılaştırması | `and` ile birleşik koşul yazabilir, aynı mantığı iç içe if ile de kurup ikisini karşılaştırabilir | pk120 | çekirdek | 031kullaniciAdiParola.py |
| pk160 | or operatörü | `or` ile "ikisinden biri yeterli" koşulunu yazabilir | pk150 | çekirdek — and ile birlikte mantıksal operatörlerin ikisi de temel dilbilgisi; or olmadan öğrenci koşul yazımının yarısını bilmez | ss03.py |
| pk170 | Pekiştirme: and ile bağımsız pratik | `and` operatörünü yeni bir problemde bağımsız kurabilir | pk150 | çekirdek | ss02.py (**tema değiştirildi**: "yaş ≥ 18 ve kurs tamamlandı → ehliyet alabilir" — orijinaldeki askerlik/cinsiyet teması kaldırıldı) |

*032: arşivde sözdizimi hatası var (`elif(*):`, `elif(/):` placeholder), script fazında düzeltilecek.

---

## 200 — while

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk210 | while temel, girinti | Koşul doğru olduğu sürece tekrar eden döngü yazabilir | pk170 | çekirdek | 100while.py, 101whileGirinti.py |
| pk220 | Sayaçla biriktirme | Sayaç değişkeniyle belirli sayıda tekrar + toplam biriktirme yapabilir (döngü içinde biriktirme, pk080'in tekrarlı hali) | pk210, pk080 | çekirdek | 102birdenOnaKadarToplamSoru.py, 105whileChallenge3Soru.py |
| pk230 | break, sentinel (durdurucu değer) | `break` ile döngüyü erken sonlandırabilir, "belirli değer girilene kadar" kalıbını kurabilir | pk220 | çekirdek | 103whileBreak.py, ss01_negatifPozitifSıfır.py |
| pk240 | continue | `continue` ile döngünün kalan gövdesini atlayıp bir sonraki tura geçebilir | pk230 | çekirdek | 104whileContinue.py |
| pk250 | while(True) + if-else pratik | Sonsuz döngüyü koşullu break ile güvenli kapatabilir | pk240 | genişletme — if-else ve while(True)+break'in ayrı ayrı zaten öğretildiği bir sentez/pratik, yeni mekanik eklemiyor | 052enBoySoru.py (**arşivde break yorum satırında kalmış, script fazında tamamlanacak**) |
| pk260 | İç içe while, desen çizimi | İki sayaçlı iç içe döngüyle satır/sütun deseni çizebilir | pk210 | çekirdek | 114stringKare.py, 115stringUcgen.py, ss04.py, ss05.py, ss06.py |
| pk270 | random modülü + while | `random.randint()` ile rastgele sayı üretip while ile koşullu üretim yapabilir | pk230 | çekirdek | 180rasgeleSayi.py, 181rasgeleTekSayiYAP.py |
| pk280 | Karma pratik: faktöriyel, sentinel toplam, modulo desenleri | Öğrenilen while kalıplarını karma bir problemde birleştirebilir | pk270 (kümülatif: pk220-270) | çekirdek | 106whileTopluSorular_Arsivle.py, ssBOM.py*, cevaplar2.1.py (BOM kısmı) |

*ssBOM: mod-7 kontrolü mantığı arşivde tutarsız (iki ayrı `if` çakışıyor), script fazında
düzeltilerek kullanılacak.

**Kaldırıldı (eski taslaktaki pk190):** "while ile listeye giriş" dersi silindi. `append()`
kullandırıyordu ama liste kavramı henüz öğretilmemişken; içeriği zaten liste ünitesindeki
"while ile liste doldurma" dersinde (pk440) var, tekrar oluyordu.

---

## 300 — for (yalnızca `range()`)

Liste burada YOK — `for eleman in liste` liste ünitesine taşındı.

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk310 | range() temelleri | `range(n)`, `range(a,b)`, `range(a,b,adım)` ile artan/azalan döngü kurabilir | pk280 | çekirdek | 150forTopluSorular_Arsivle.py (ss1, ss2 kısmı) |
| pk320 | for ile biriktirme, faktöriyel | for içinde sayaç olmadan toplam/çarpım biriktirebilir | pk310 | çekirdek | 150forTopluSorular_Arsivle.py (ss3, ss4 kısmı) |
| pk330 | for'un sınırı: ne zaman while kullanılır | "Kaç kez tekrarlanacağı belliyse for, belli değilse while" ayrımını yapıp aynı problemi doğru araçla çözebilir | pk320, pk230 | çekirdek — arşivde tekrar eden bir hata kalıbını (`iter(int,1)`) doğrudan düzeltiyor; for/while seçimi öğrencinin bundan sonraki her problemde karşılaşacağı bir karar noktası | YENİ — 150forTopluSorular_Arsivle.py'nin ss5 kısmındaki `for _ in iter(int,1)` kalıbının (seviye üstü, arşivde işaretli) karşı-örnek olarak kullanılması |
| pk340 | İç içe for: çarpım tablosu | İç içe while'dan (pk260) transfer ederek range ile iç içe döngü kurup çarpım tablosu gibi klasik bir problemi çözebilir | pk310, pk260 | çekirdek | YENİ |

---

## 400 — liste

`for eleman in liste` bu ünitede öğretiliyor (300'den taşındı).

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk410 | Liste nedir, oluşturma, index | Liste oluşturabilir, pozitif/negatif index ile elemana erişebilir | pk340 | çekirdek | ssdiziTekrar_Arsivle.py (liste[0], liste[-1] kısmı) + YENİ (liste tanıtımı) |
| pk420 | for ile liste üzerinde gezinme | `for eleman in liste` ile bir listenin elemanlarını index kullanmadan gezebilir | pk410, pk310 | çekirdek | 185listeDizi1.py |
| pk430 | Dilimleme (slicing) | `liste[a:b]` ile alt liste alabilir | pk410 | çekirdek | ssdiziTekrar_Arsivle.py (slicing kısmı) |
| pk440 | while ile liste doldurma | while döngüsünde `append()` ile listeyi doldurabilir, birden fazla çözüm yolunu karşılaştırabilir | pk430, pk230 | çekirdek | ssdiziTekrar_Arsivle.py (mirsad/selim kod kısmı) |
| pk450 | for ile liste doldurma | for döngüsünde (range ile) `append()` ile n elemanlı liste doldurabilir | pk430, pk320, pk440 (append()'in öğretildiği yer), pk330 (for/while kuralı) | çekirdek | 186DiziyeKlavyedenVeriGirisiYAP.py |
| pk460 | Index atamasıyla liste doldurma | `[0]*n` ile boş liste oluşturup index ataması yapabilir (append'siz yöntem) | pk410, pk440 (append() referansı, contrast için) | genişletme — listeyi doldurmanın üçüncü yolu; 440 ve 450'de iki yöntem zaten öğretildi, yeni kazanım eklemiyor | genelTekrar0_bosDizi.py |
| pk470 | Liste analiz sentezi: sayma, toplam, ortalama | Girilen verileri listede toplayıp sayma/toplam/ortalama analizi yapabilir | pk440, pk450 | çekirdek | genelTekrar01_diziWhile.py (cevaplar2.1.py'de benzer bir soru var, referans) |

---

## 500 — string metodları

Dosya işlemleri (open/write/read) buradan çıkarıldı, kendi kapanış ünitesine (800) taşındı.

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk510 | len(), find() | Bir string'in uzunluğunu bulabilir, içinde geçen bir alt metnin konumunu bulabilir | pk470 | çekirdek | 305farkliMetodlar.py (len, find kısmı) |
| pk520 | upper(), lower() | String'i büyük/küçük harfe çevirebilir. **Geri bağlantı:** pk160'ta (`ss03.py`) `cevap=="ersoy" or cevap=="Ersoy" or cevap=="ERSOY"` diye üç kez `or` yazmıştık — `.lower()` ile artık gerekmiyor. Öğrenci metodun neden var olduğunu tanımdan değil, çektiği sıkıntıdan öğreniyor | pk510, pk160 | çekirdek — pk160'ta üç kez `or` ile çözülen problemin gerçek çözümü burada; salt tanım değil, somut bir ihtiyacın karşılığı | 305farkliMetodlar.py (upper, lower kısmı) |
| pk530 | split(), strip() | String'i parçalara ayırabilir, baştaki/sondaki boşlukları temizleyebilir | pk510, pk410 (liste index, `kelimeler[0]` için) | genişletme — kullanışlı ama sonraki hiçbir dersin kazanımı bu metodları zorunlu kılmıyor | YENİ |
| pk540 | String indexleme ve dilimleme | Liste ile paralel olarak string'i index/slice edebilir | pk410, pk430 | çekirdek | YENİ |
| pk550 | f-string ile biçimlendirme | `f"..."` ile değişkenleri okunaklı biçimde string içine gömebilir | pk510, pk020 | çekirdek — arşivdeki ss dosyaları f-string'i zaten kullanıyor, formal ders yoksa öğrenci gördüğü kodu okuyamaz | YENİ |
| pk560 | Pekiştirme: string + for sentezi | for ile string karakterlerini gezip sayma/tersten yazdırma/palindrome gibi problemleri çözebilir | pk540, pk320, pk420 (for eleman in liste/string, temel dayanak), pk520 (upper(), SEN YAP'ta) | çekirdek | YENİ |

---

## 600 — fonksiyon

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk610 | Fonksiyon tanımı, parametre, return | `def` ile fonksiyon tanımlayıp parametre alıp return ile sonuç döndürebilir | pk560, pk040 | çekirdek | 500fonksiyon00.py |
| pk620 | Tek parametreli fonksiyon, pratik | Gerçek bir problemi (daire alanı) fonksiyon olarak yazabilir | pk610 | genişletme — 610'daki tanımın ilk uygulaması; 630 zaten farklı bir pratik örnek sağlıyor | 501fonksiyon01.py (arşivde `r**2` vardı, öğretilmediği için `r*r` yapıldı) |
| pk630 | Bool döndüren fonksiyon | Fonksiyondan `True`/`False` döndürüp çağıran tarafta if ile kullanabilir | pk610, pk280 (`%`), pk110 (karşılaştırmanın True/False döndürdüğü yer) | çekirdek | 502fonksiyon.py |
| pk640 | Fonksiyon + if-elif-else sentezi | Fonksiyon içinde çok koşullu mantık kurabilir | pk630, pk610, pk130, pk550 (f-string) | genişletme — fonksiyon ile elif zincirini birleştiren iyi bir sentez ama iki parça da ayrı ayrı zaten öğretildi (610, 130) | genelTekrar03_def.py (arşivde `num**2` vardı, öğretilmediği için `num*num` yapıldı) |
| pk650 | Fonksiyona parametre olarak liste, return liste | Listeyi parametre alıp for ile işleyip yeni liste return edebilir | pk610, pk450, pk440 (append()'in öğretildiği yer), pk420 (for eleman in liste) | çekirdek — fonksiyon ve liste ünitelerini birleştiren tek ders; atlanırsa iki ünite birbirine hiç bağlanmamış olur | 503fonksiyon.py (yorumdaki list comprehension "diğer yol" bir not olarak gösterilir, ayrı ders açılmadı) |
| pk660 | Varsayılan parametre değerleri | Parametreye varsayılan değer atayabilir | pk610 | çekirdek | YENİ |

---

## 700 — sözlük (dict)

Arşivde hiç yok, tamamen **YENİ**.

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk710 | dict nedir, oluşturma | key-value çifti ile dict oluşturabilir | pk660 | çekirdek | YENİ |
| pk720 | Erişim, ekleme, güncelleme | `dict[key]` ile okuyup yazabilir, yeni key ekleyebilir | pk710 | çekirdek | YENİ |
| pk730 | Silme, key kontrolü | `del`, `in` operatörüyle key varlığını kontrol edip silebilir | pk720 | çekirdek | YENİ |
| pk740 | for ile dict gezme | `.keys()`, `.values()`, `.items()` ile dict'i gezebilir | pk730, pk420 | çekirdek | YENİ |
| pk750 | Basit uygulama: sözlük/rehber | dict ile küçük bir sözlük veya telefon rehberi uygulaması yazabilir | pk740 | çekirdek | YENİ |
| pk760 | Liste içinde dict: kayıt yapısı | Kayıt yapısını (öğrenci bilgisi gibi) liste + dict ile modelleyebilir | pk750, pk450 | genişletme — iç içe veri yapısı ileri bir kavram; temel dict kullanımı (710-750) bunsuz da tamamlanmış olur | YENİ |
| pk770 | dict ile sayma/gruplama | Kelime sayma gibi klasik problemi dict ile çözebilir | pk740, pk560 | genişletme — faydalı bir kalıp ama ünitenin çekirdek kazanımı (710-750) buna bağlı değil, kapanışa yakın olduğu için zaman kısıtında ilk kesilecekler arasında | YENİ |

---

## 800 — dosya işlemleri (kapanış ünitesi)

| pk | Konu | Kazanım | Önkoşul | Öncelik | Kaynak |
|---|---|---|---|---|---|
| pk810 | Dosyaya yazma, dosyadan okuma | `open()`/`write()`/`read()` (`with` ile) kullanabilir | pk560 | çekirdek | 305farkliMetodlar.py (dosya kısmı) |
| pk820 | Dosyayı satır satır okuma | `readlines()` veya for ile dosyayı satır satır işleyebilir | pk810, pk320 | genişletme — 810'daki temel oku/yaz zaten çekirdek kazanım; yıl sonuna denk geliyorsa ilk atlanacak | YENİ |

---

## İleri seviye — kapsam dışı

9. sınıf seviyesini aşıyor, müfredata girmiyor. Arşivden silinmedi, sadece ayrıldı.

| Dosya | Neden kapsam dışı |
|---|---|
| genelTekrar04_ChainOfResponsibility.py | OOP tasarım deseni (class, kalıtım) |
| genelTekrar06_enum.py | Enum |
| genelTekrar06_enum2.py | Enum + dış kütüphane (`keyboard`) |
| genelTekrar06_normalModOzelMod_enum.py | Enum + match-case (Python 3.10+ ileri sözdizimi) |
| genelTekrar06_if.py | Enum serisinin "enum'suz önce" örneği — enum dışarıda kaldığı için anlamsız kalıyor |
| genelTekrar05_normalModOzelMod.py | try/except + durum makinesi (state machine) |
| genelTekrar02_diziWhileFor.py | `enumerate()` — 9. sınıf giriş dersi için gereksiz görüldü |
| vocabulary91.py | Dış kütüphane (`edge_tts`, `asyncio`), TTS ses üretimi — Python değil İngilizce ders materyali |
| vocabulary91.txt | vocabulary91.py'nin veri dosyası, aynı grupla ayrıldı |

**Kullanılmayan (duplicate/bozuk, kapsam dışı değil ama müfredatta ayrı yer almıyor):**
002string.....py (001 ile aynı), Untitled-1.py (021 ile neredeyse aynı),
genelTekrar04_dosyaMetodlari.py (305farkliMetodlar.py'nin Türkçe karakterleri bozulmuş kopyası).

---

## Arşivde tespit edilen hatalar (script fazında düzeltilecek)

- **032hesapMakinesiCevapBITMEDI.py:** `elif(*):`, `elif(/):` geçersiz sözdizimi — placeholder,
  çalıştırılamaz. pk140'ta kaynak olarak kullanılırken düzeltilecek.
- **ssBOM.py:** mod-7 kontrolü mantığı tutarsız (iki ayrı `if` birbiriyle çakışıyor, orijinal
  amacı muhtemelen "her 7 sayıda bir BOM yazdır"). pk280'de kaynak olarak kullanılırken
  düzeltilecek.
- **052enBoySoru.py:** `break` mantığı yorum satırında (`'''...'''`) bırakılmış, dosya
  sonsuz döngüde kalacak şekilde bitmemiş. pk250'de tamamlanacak.

---

Onaylanan dört düzeltme: (1) pk340'ın önkoşuluna pk260 eklendi — iç içe döngü while'dan
for'a transfer ediliyor artık açıkça yazılı; (2) pk520'ye pk160/ss03.py'ye geri bağlanma notu
eklendi; (3) pk045 "hata mesajı okuma" dersi eklendi, pk110'a IndentationError geri-bağlantı
notu düşüldü; (4) her derse çekirdek/genişletme etiketi ve tek cümlelik gerekçe eklendi.

Üretime geçmeden eklenen son iki düzeltme: (A) çok satırlı yorum (`'''...'''`) pk050'den
pk020'ye taşındı — her scriptin docstring'i pk010'dan itibaren görüleceği için atlanamaz;
pk050 sadece `*` gözlemi olarak genişletme kaldı. (B) ünite düzeyinde ayrı bir öncelik
eklendi (Ünite planı tablosu) — ders düzeyindeki "46 çekirdek" sayısı, kendi içinde kapalı
zincirleri olan 700/800 gibi üniteleri de çekirdek gösterdiği için yanıltıcıydı; artık
000-600 çekirdek ünite, 700 ve 800 genişletme ünitesi olarak ayrı işaretli.

**Onaylandı, FAZ 2 üretimi başladı.** Ünite ünite ilerleniyor, her ünite bitince durup
`backlog.md` güncellenip onay bekleniyor.

**FAZ 2 sırasında bulunan önkoşul grafiği eksikleri:** pk450'nin Önkoşul'una pk440 (append()'in
öğretildiği yer) ve pk330 (for/while kuralı) eklendi; pk460'ın Önkoşul'una pk440 eklendi
(script gövdesinde "pkXXX'te öğrendiğin" diye atıf yapılan her ders, artık Önkoşul satırında
da var — script ile mufredat senkron).

**500 ünitesinde bulunan genişletme geri-bağlantı riski:** pk540, ilk yazımda genişletme olan
pk460'a "hatırla" diye atıf yapıyordu (liste elemanı değiştirme örneği); pk460 kesilirse bu
atıf boşa düşerdi. Örnek pk540'ın kendi içine taşındı (liste[0]=99 satırı eklendi), artık
pk460'a hiç yaslanmıyor. Ayrıca pk550'nin Önkoşul'undaki pk030 (genişletme) gereksizdi —
asıl dayanak pk020'ydi (çekirdek), pk030 referansı kaldırıldı. pk520'nin Önkoşul'una da
Kazanım'da zaten anlatılan pk160 bağlantısı eklendi (script ile mufredat senkron değildi).

**Önkoşul taramasının iki türü:** pk530'da açık atıf (pk410, "hatırla") kaçmıştı, eklendi.
pk560'ta ise örtük bağımlılıklar (pk420 for-eleman-in-liste'nin temel dayanağıydı, pk520
SEN YAP'ta upper() için) hiç yakalanmamıştı — çünkü orada hatırlatacak bir pkXXX metni yoktu.
Ayrıca pk560'ın KAVRAM'ı kendi öğrettiği "for eleman in X" yöntemini terk edip index-tabanlı
`range(len(kelime)-1,-1,-1)`'e dönüyordu (üstelik üç argümanlı, içinde iki farklı anlamda -1
olan bir kalıp) — tek bir `for harf in kelime: ters = harf + ters` döngüsüyle sadeleştirildi,
artık dersin kendi yöntemiyle tutarlı ve len() de gereksiz hale geldiği için Önkoşul'dan çıktı.

**600 ünitesi (fonksiyon):** Önkoşul satırları baştan (a)/(b) kuralına göre kuruldu, sonradan
tarama yapılmadı. İki arşiv dosyasında (`501fonksiyon01.py`, `genelTekrar03_def.py`) hiç
öğretilmemiş `**` (üs alma) vardı, ikisi de `*` ile değiştirildi. pk630, pk640, pk650'nin
gövdesinde geçen her `pkXXX` (pk110, pk610, pk440 dahil) doğrudan Önkoşul'a yazıldı — transitif
olarak zincirden ulaşılabilir olsalar bile, script kendi başına okunduğunda dayandığı her ders
görünür olsun diye.
