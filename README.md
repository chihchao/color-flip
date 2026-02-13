# Color Flip 🎨

### 一個專為色彩原理教學設計的雙向互動工具 (RGB ↔ HSB)

`Color Flip` 是一個基於 Python 與 Gradio 開發的輕量化互動程式。它旨在幫助學生與設計師理解數位色彩底層的 **RGB (硬體邏輯)** 與人類直覺的 **HSB (設計邏輯)** 之間是如何相互轉換與連動的。

線上示範：<https://cchsu-course-color-flip.hf.space/>

## 核心特色

* **雙向連動 (Real-time Sync)**：調整 RGB 滑桿，HSB 數值隨之改變；反之亦然，完美模擬 Figma 的顏色選擇器。
* **視覺化回饋**：即時預覽顏色變化，直觀感受「飽和度」與「亮度」對色彩的影響。
* **教學友善**：簡潔的 UI 配置，適合在課堂上展示色彩三要素（色相、飽和度、亮度）的數學本質。
* **零部署啟動**：支援直接在 Google Colab 或在地端環境一鍵運行。

## 核心原理

本程式展示了以下色彩科學的核心概念：

1. **Hue (色相)**：由 RGB 的相對比例決定其在  色輪上的位置。
2. **Saturation (飽和度)**：RGB 數值之間的差距大小。
3. **Brightness (亮度)**：RGB 數值的整體強度。

## 快速開始

### 前置要求

確保您的環境已安裝 Python 3.8+ 以及 `gradio` 庫。

```bash
pip install gradio

```

### 執行程式

1. 下載 `color_flip.py`。
2. 在終端機執行：
```bash
python color_flip.py

```


3. 點擊產生的 `http://127.0.0.1:7860` 連結即可開始操作。

