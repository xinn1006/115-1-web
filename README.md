# 115-1 網頁程式設計 (Web Programming)

本專案為 115-1 學期「網頁程式設計」實作課程專案庫，主要基於 **Python 3.10+** 與 **Django 4.x** 框架，透過循序漸進的實作單元學習 Web 應用程式開發、Django MVT 架構、資料庫 ORM 操作與前端模板繼承技術。

---

## 📚 各章節實作內容說明

### 🔹 CH1: Django 基礎建置 (`dj4ch01`)
* Django 專案與 App 初始化（`mysite`）。
* 認識基本路由機制（`urls.py`）與檢視函式（`views.py`）。
* 熟悉 `manage.py` 命令列工具與內建開發伺服器運行機制。

### 🔹 CH2: 部落格系統與樣版繼承 (`dj4ch02`)
  * 建立經典部落格範例專案 `mblog`。
  * 實作文章資料庫模型（`models.py`）與資料庫遷移。
  * 建立模組化模板架構（`base.html`、`header.html`、`footer.html`、`index.html`、`post.html`）。
  * 撰寫自訂 Template Tag（`markdown_extras.py`），支援 Markdown 語法解析與渲染。
  * 靜態資源配置（CSS、圖片與 Logo）。

### 🔹 CH4: 資料模型擴充與 ORM 遷移 (`dj4ch04`)
  * 深入了解 Django ORM 的 Schema 演進與多階段遷移（Migrations）：
    * 新增自訂資料表（`NewTable`）
    * 建立產品資料表（`Product`）
    * 變更產品規格欄位（`alter_product_size`）
    * 新增產品庫存欄位（`product_qty`）
  * 擴充多頁面展示功能：
    * 產品清單頁面（`list.html`）
    * 詳細規格展示（`disp.html`）
    * 關於我們頁面（`about.html`）

### 🔹 CH5: 資料篩選與汽車展示應用 (`dj4ch05`)
  * 實作進階資料庫查詢（QuerySet Filter、條件排序）。
  * 汽車展示與價格篩選系統：
    * 車輛資訊清單（`carlist.html`）
    * 價格區間過濾與動態查詢（`carprice.html`）
  * 強化視圖（View）與資料庫之間的資料互動與邏輯處理。

---

## 🛠️ 開發環境與技術棧

* **開發語言**：Python 3.10+
* **後端框架**：Django 4.x
* **資料庫**：SQLite 3
* **環境管理**：Conda (Anaconda / Miniconda)
* **前端技術**：HTML5, CSS3, JavaScript, Django Template Engine

---

## 🚀 專案啟動方式 (使用 Conda)

本專案各章節皆為獨立的 Django 專案，請先透過 Conda 建立專屬虛擬環境，再進入目標章節目錄執行。

### 1. 複製專案庫
```bash
git clone https://github.com/xinn1006/115-1-web.git
cd 115-1-web
```

### 2. 建立並啟動 Conda 虛擬環境
建議指定 Python 3.10 版本建立獨立環境：
```bash
# 建立 Conda 虛擬環境
conda create -n myvenv python=3.10 -y

# 啟動虛擬環境
conda activate myvenv
```

### 3. 安裝相依套件
啟動 Conda 環境後，可直接安裝第一章提供的套件清單或手動安裝核心套件：
```bash
# 方式 A：透過專案內的 requirements.txt 安裝
pip install -r dj4ch01/requirements.txt

# 方式 B：手動安裝 Django 與 Markdown 渲染套件
pip install django markdown
```

### 4. 選擇章節並進入對應專案目錄
各章節的 `manage.py` 所在目錄如下表所示：

| 章節 | 專案路徑 | 進入指令 |
| :--- | :--- | :--- |
| **CH1** | `dj4ch01/` | `cd dj4ch01` |
| **CH2** | `dj4ch02/mblog/` | `cd dj4ch02/mblog` |
| **CH4** | `dj4ch04/mblog/` | `cd dj4ch04/mblog` |
| **CH5** | `dj4ch05/mblog/` | `cd dj4ch05/mblog` |

> 💡 **提示**：若目前已在某章節內部，要切換至其他章節，可先返回根目錄（如 `cd ../..`）再進入目標路徑。

### 5. 資料庫遷移與初始化
進入該章節資料夾後，執行以下指令確認資料庫表結構為最新：
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 建立後台管理員帳號 (選用，Create Superuser)
若需登入 Django 管理後台新增或檢視資料：
```bash
python manage.py createsuperuser
```
*(依終端機提示輸入 Username、Email 與 Password)*

### 7. 啟動本機開發伺服器 (Run Server)
```bash
python manage.py runserver
```

伺服器啟動後，使用瀏覽器開啟以下網址：
* **前台首頁**：[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **管理後台**：[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### 8. 停止伺服器與退出 Conda 環境
* **停止開發伺服器**：在終端機按下 `Ctrl + C`
* **退出 Conda 環境**：
  ```bash
  conda deactivate
  ```
