"""
pk730 çözümü — Silme, key kontrolü
"""

kitap = {"ad": "Küçük Prens", "yazar": "Antoine de Saint-Exupéry", "sayfa": 96, "yil": 1943}

print("yil" in kitap)

del kitap["sayfa"]

print("sayfa" in kitap)
