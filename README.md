# 🌍 Beyaz Barış Hava Koridoru — YSCS v1

**"Yurtta Sulh Cihanda Sulh"** — *Peace at Home, Peace in the World*

Bir interaktif 3D dünya görselleştirme projesi. Küresel barış koridorlarını, ticaret rotalarını, enerji pipeline'larını ve uluslararası şehir ağlarını sinematik bir deneyimle sunan web uygulaması.

---

## 📋 Özellikler

### 🎬 **TOS (Tam Otomatik Sinema)**
- Tek tıkla tam otomatik cinematic deneyim başlat
- Güneş/ay döngüsü, müzik, tüm turlar otomatik oynatılır
- Engel taşıyıcı ve koridorlar otomatik senkronize edilir
- Temiz sinematik görünüm (tüm UI gizlenir)

### 🏙️ **YSCS Modu** 
- Şehir isimlerinin antik dil çevirileri ile hover modu
- "Yurtta Sulh Cihanda Sulh" felsefesini etkileşimli şekilde keşfet

### 🌐 **8 Coğrafi Katman**
1. **Beyaz Kuşak** — Ana barış koridoru (beyaz)
2. **Atlantik** — Batı-Doğu bağlantısı (yeşil)
3. **Akdeniz-Afrika** — Ay-Sahara rotası (turuncu)
4. **Pasifik-Asya** — Asya-Pasifik ağı (mavi)
5. **Amerika** — Trans-Atlantik merkezi (pembe)
6. **Batı Afrika** — Sahel koridoru (sarı)
7. **Orta Asya** — İpek Yolu mirası (cyan)
8. **Pasifik-Güney** — Güney Pasifik hattı (yeşil)

### ⚡ **Görsel Elemanlar**
- **DNA Çift Helix Enerji Akışı** — Renkli parçacıklar ile dinamik enerji taşımacılığı
- **Merkez Kaçkın Radyaller** — Karada enerji yayılımı
- **İnter-Şehir Bağlantıları (TNB)** — Tüm noktalar arası ağ
- **Uçak/Gemi/Tren/Kamyon Simülasyonu** — Gerçek zamanlı trafik
- **Gece Işıkları Katmanı** — NASA uydu görüntüleri

### 🎮 **İnteraktif Kontroller**
- **Dönüş Hızı** — Küre rotasyonunu kontrol et (0x - 4x)
- **Güneş Konumu** — Gündüz/Gece döngüsü
- **Koridim Genişliği** — 1000km - 3000km arası ayarlı
- **Küre Saydamlığı** — Atmosfer görünürlüğü
- **TNB Yoğunluğu** — Inter-city connections oranı
- **Zoom Seviyeleri** — Yakın/Orta/Uzak görünümler

### 🎵 **Müzik**
- Ambient müzik: `12 Dil v4.wav`
- Otomatik başlar (TOS modu)
- Manuel açıp kapat butonuyla kontrol

### 📸 **Ek Özellikler**
- Ekran görüntüsü alma (PNG)
- Şehir navigasyonu (12 ana şehir)
- Koridim renk dinamiği (gece/gündüz senkron)
- Legends & Stats paneli

---

## 🚀 Kullanım

### Tarayıcıda Aç
```bash
# Basit HTTP sunucu ile çalıştır
python3 -m http.server 8000
# Sonra: http://localhost:8000
```

### Tuşlar & Butonlar

| Buton | Fonksiyon |
|-------|----------|
| 🎥 **TOS** | Tam Otomatik Sinema (hepsi birlikte) |
| **YSCS** | Şehir Hover Modu (antik diller) |
| **🎬 Tümü** | Tüm turları oynat |
| **🌙▶️** | Güneş otomatik olarak hareket |
| **🎵** | Müzik aç/kapat |
| **📸** | Ekran görüntüsü indir |

### Tur Butonları
- ⬜ **BK** — Beyaz Kuşak Turu
- 🟢 **AT** — Atlantik Turu
- 🟠 **AK** — Akdeniz-Afrika Turu
- 🔵 **PA** — Pasifik-Asya Turu
- 🟣 **AM** — Amerika Turu
- 🟡 **BA** — Batı Afrika Turu
- 🔵 **OA** — Orta Asya Turu
- 🟢 **PG** — Pasifik-Güney Turu

---

## 📁 Dosya Yapısı

```
world-yscs-v1/
├── index.html           # Ana uygulama (Three.js + HTML/CSS/JS)
├── music/
│   └── 12 Dil v4.wav   # Ambient müzik dosyası
├── fix.py              # Temizleme scripti
└── README.md           # Bu dosya
```

---

## 🛠️ Teknik Stack

- **Three.js** — 3D küre ve grafik
- **Tailwind CSS** — UI styling
- **Vanilla JavaScript** — Etkileşim ve animasyonlar
- **HTML5 Audio** — Müzik oynatıcısı
- **Canvas API** — Parçacık efektleri

---

## 🌟 İlham & Konsept

**Atatürk Cümlesi**: *"Yurtta Sulh, Cihanda Sulh"* 

Bu proje, küresel barış, işbirliği ve uluslararası bağlantıların ihtişamlı bir görselleştirmesidir. Enerji akışlarından ticaret rotalarına, antik şehirlerden modern ağlara — hepsi bir harmonik bütün halinde.

---

## 📝 Notlar

- Müzik dosyası `music/` klasöründe yüklü olmalıdır
- Tarayıcı desteği: Modern Chrome, Firefox, Safari, Edge
- Mobil cihazlarda optimize edilmiştir
- GPU hızlandırma önerilir

---

## 👨‍💻 Geliştirici

**DJ-Shaman's World** — Interactive Peace Corridor Visualization

---

## 📜 Lisans

MIT License — Özgürce kullan, değiştir, dağıt.
