# Backlog Log — append-only geçmiş

Backlog'dan silinen her madde tarihiyle buraya eklenir. Hiçbir şey silinmez.

## 2026-09-02

- Proje iskeleti kuruldu: CLAUDE.md, AGENTS.md, backlog.md, backlog-log.md, notes.md, git init, GitHub public repo.
- Müfredat (`mufredat.md`) yazıldı, revize edildi, onaylandı: 9 ünite (000-800), 57 ders,
  47 çekirdek + 10 genişletme.
- FAZ 2 (script üretimi) tamamlandı: 57 script + 57 çözüm (`cozumler/`), ünite ünite yazılıp
  denetlenip onaylandı. Yol boyunca kalıcı hale gelen kurallar (hepsi CLAUDE.md/AGENTS.md'de):
  sessizce kullanma yok (satır düzeyinde önkoşul — bağımlılık/hatırlatma ayrımıyla), açıklama
  kontrolü kod kontrolünden ayrı, genişletme dersine geri-bağlantı koşullu.
- Müfredat geneli bütünlük denetimi yapıldı ve Özgür tarafından doğrulandı: mufredat.md/script
  eşleşmesi, önkoşul grafiği geçerliliği, çekirdek/genişletme sayıları, sessizce kullanma
  taraması (str/float/round/**/items/keys/values/split/strip), 114 dosyanın py_compile testi.
  Son iki küçük düzeltme (pk260→pk150 önkoşulu, pk460'ın pk050'ye gereksiz atfının kaldırılması)
  ile müfredat kapandı.

## 2026-10-04

- "BU KOD NE YAPAR?" bloğu kuralı eklendi (ak'deki kuralın pk uyarlaması, zihinev-3f üzerinden
  Özgür onayıyla): her `pk*.py`'nin başında, başlık docstring'inden önce 2-3 satırlık `#` bloğu;
  onar alıştırmalarında yalnız amaç, `cozumler/` kapsam dışı. CLAUDE.md ve AGENTS.md "Sert
  sınırlar"a aynı metinle işlendi.
- 57 scriptin hepsine blok eklendi (kod okunarak yazıldı), tümü py_compile ile derleniyor.
  pk045 onar değil kasıtlı çöken ders olduğundan çöküş bloğa açık yazıldı. Çıktı karşılaştırması
  yapılmadı. Commit'ler: 2d0a00b (köprü bloğu + kimlik_pk.txt), 5689bd7 (kural + 57 script).
