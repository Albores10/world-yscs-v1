# 🌍 Beyaz Barış Hava Koridoru — YSCS v1

**"Yurtta Sulh Cihanda Sulh"** — *Peace at Home, Peace in the World*

İnteraktif 3D dünya görselleştirme projesi. Küresel barış koridorlarını, ticaret rotalarını, enerji pipeline'larını ve uluslararası şehir ağlarını sinematik bir deneyimle sunan tek sayfa web uygulaması.

🔗 **Canlı:** [albores10.github.io/world-yscs-v1](https://albores10.github.io/world-yscs-v1/)

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

### 🌐 **9 Coğrafi Katman**

| # | Hat | Renk | Rota |
|---|-----|------|------|
| 1 | **Beyaz Kuşak (BK)** | ⬜ Beyaz | Tokyo → Seul → Gansu → Aksu → Buhara → Bakü → Ankara → Roma → Madrid → Turks ve Caicos → Meksika → Honolulu *(yatay halka)* |
| 2 | **Atlantik (AT)** | 🟢 Yeşil | Vaşington → Karakas → Belem → Rio de Janeiro |
| 3 | **Akdeniz-Afrika (AK)** | 🟠 Turuncu | Budapeşte → Kahire → Hartum → Mogadişu → Dar es Salaam → Antananarivo → Cape Town |
| 4 | **Pasifik-Asya (PA)** | 🔵 Mavi | Ulanbatur → Gansu → Hong Kong → Bangkok → Cakarta |
| 5 | **Amerika (AM)** | 🩷 Pembe | San Francisco → Meksika → Panama → Lima → Santiago |
| 6 | **Batı Afrika (BA)** | 🟡 Sarı | Londra → Madrid → Marakeş → Dakar → Lagos → Luanda |
| 7 | **Kafkasya-Kızıl Deniz (OA)** | 🩵 Cyan | Moskova → Bakü → Karaçi |
| 8 | **Kuzey-Güney Barış (KG)** | 🟣 Mor | Astana → Buhara → Lahor → Tripura |
| 9 | **Pasifik-Güney (PG)** | 🍏 Yeşil | Tokyo → Tayvan → Cebu → Nabire → Sydney → Tauranga |

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
- 5 ambient parça: `12 Dil v1` → `v2` → `v3` → `v4` → `v5`
- Parça bitince otomatik sonrakine geçer (döngü)
- TOS modunda otomatik oynatılır
- ◀ ▶️ ▶ butonlarıyla manuel kontrol

### � **Mobil Uyumluluk**
- Mobil öncelik responsive tasarım (640px / 980px kırılımları)
- Tur ve şehir satırları yatay kaydırmalı
- Dokunmatik ekran için büyütülmüş buton alanları
- Alt bar, yan paneller mobilde yeniden konumlanır

### 📸 **Ek Özellikler**
- Ekran görüntüsü alma (PNG)
- Şehir navigasyonu (hızlı geçiş butonları)
- Koridor genişlik dinamiği (gece/gündüz senkron)
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
| **YSCS** | Şehir Hover Modu (barış sözleri) |
| **🎬 Tümü** | Tüm turları sırayla oynat |
| **🌙 ▶️** | Güneş konumunu otomatik ilerlet |
| **◀ ▶️ ▶** | Müzik önceki / oynat / sonraki |
| **📸** | Ekran görüntüsü indir (PNG) |

### Tur Butonları
- ⬜ **BK** — Beyaz Kuşak (ana yatay halka)
- 🟢 **AT** — Atlantik
- 🟠 **AK** — Akdeniz-Afrika
- 🔵 **PA** — Pasifik-Asya
- 🟣 **AM** — Amerika
- 🟡 **BA** — Batı Afrika
- 🔵 **OA** — Kafkasya-Kızıl Deniz
- 🟣 **KG** — Kuzey-Güney Barış
- 🟢 **PG** — Pasifik-Güney

---

## 📁 Dosya Yapısı

```
world-yscs-v1/
├── index.html           # Ana uygulama (Three.js + HTML/CSS/JS, tek dosya)
├── music/
│   ├── 12 Dil v1.wav   # Ambient müzik — 1. parça
│   ├── 12 Dil v2.wav   # Ambient müzik — 2. parça
│   ├── 12 Dil v3.wav   # Ambient müzik — 3. parça
│   ├── 12 Dil v4.wav   # Ambient müzik — 4. parça
│   └── 12 Dil v5.wav   # Ambient müzik — 5. parça
├── fix.py              # Yardımcı script
└── README.md           # Bu dosya
```

---

## 🛠️ Teknolojiler

- **Three.js r128** — 3D WebGL render
- **Tailwind CSS (CDN)** — Yardımcı CSS sınıfları
- **HTML5 Audio API** — Müzik oynatıcı
- **Vanilla JS** — Tüm interaktif mantık
- **Canvas API** — Dinamik dokular (şehir etiketleri, parçacıklar)

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
