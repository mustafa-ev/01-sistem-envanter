import platform
import socket
import json
import psutil

def sistem_bilgilerini_al():
    bilgi = {
        "hostname": socket.gethostname(),
        "ip_adresi": socket.gethostbyname(socket.gethostname()),
        "isletim_sistemi": platform.system(),
        "isletim_sistemi_surum": platform.release(),
        "islemci": platform.processor(),
        "ram_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "disk_kullanimi_yuzde": psutil.disk_usage('/').percent
    }
    return bilgi

# Doğrudan çalıştırma bloğu
print("Sistem bilgileri toplanıyor...")
veri = sistem_bilgilerini_al()

with open("envanter.json", "w", encoding="utf-8") as dosya:
    json.dump(veri, dosya, indent=4, ensure_ascii=False)

print("BAŞARILI: 'envanter.json' dosyası bulunduğunuz klasöre kaydedildi!")