\# System Inventory \& Collector Script



Bu proje, yerel veya uzak sunucuların sistem donanım, disk ve ağ yapılandırma bilgilerini otomatik olarak toplayan ve zaman damgalı JSON formatında raporlayan bir Python otomasyon aracıdır.



\## Özellikler

\* \*\*Sistem Bilgileri:\*\* OS sürümü, İşlemci, Çekirdek sayısı ve Toplam RAM.

\* \*\*Disk Analizi:\*\* Tüm mantıksal sürücülerin toplam, kullanılan ve boş alan (GB) durumları.

\* \*\*Ağ Yapılandırması:\*\* Aktif ağ kartları, IPv4 adresleri ve MAC adresleri.

\* \*\*Dinamik Raporlama:\*\* Tarih bazlı otomatik JSON çıktı üretimi.



\## Gereksinimler

\* Python 3.x

\* `psutil` kütüphanesi



\## Kullanım

Gerekli bağımlılığı yükleyin:

```bash

pip install psutil

