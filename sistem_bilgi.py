import platform
import socket
import json
import psutil
from datetime import datetime

def ag_bilgilerini_al():
    ag_kartlari = {}
    addrs = psutil.net_if_addrs()
    for arabirim, adres_listesi in addrs.items():
        ag_kartlari[arabirim] = []
        for adres in adres_listesi:
            if adres.family == socket.AF_INET:  # IPv4
                ag_kartlari[arabirim].append({"ip": adres.address, "netmask": adres.netmask})
            elif hasattr(psutil, 'AF_LINK') and adres.family == psutil.AF_LINK:  # MAC
                ag_kartlari[arabirim].append({"mac": adres.address})
    return ag_kartlari

def disk_bilgilerini_al():
    diskler = []
    for bolum in psutil.disk_partitions():
        try:
            kullanim = psutil.disk_usage(bolum.mountpoint)
            diskler.append({
                "surucu": bolum.device,
                "toplam_gb": round(kullanim.total / (1024**3), 2),
                "kullanilan_gb": round(kullanim.used / (1024**3), 2),
                "bos_gb": round(kullanim.free / (1024**3), 2),
                "yuzde": kullanim.percent
            })
        except PermissionError:
            continue
    return diskler

def detayli_envanter_topla():
    zaman = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    envanter = {
        "rapor_tarihi": zaman,
        "sistem": {
            "hostname": socket.gethostname(),
            "isletim_sistemi": f"{platform.system()} {platform.release()}",
            "islemci": platform.processor(),
            "cekirdek_sayisi": psutil.cpu_count(logical=True),
            "toplam_ram_gb": round(psutil.virtual_memory().total / (1024**3), 2)
        },
        "disk_durumu": disk_bilgilerini_al(),
        "ag_yapilandirmasi": ag_bilgilerini_al()
    }
    
    dosya_adi = f"envanter_{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(envanter, f, indent=4, ensure_ascii=False)
        
    print(f"Gelişmiş envanter raporu oluşturuldu: {dosya_adi}")

if __name__ == "__main__":
    detayli_envanter_topla()