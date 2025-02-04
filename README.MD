# 檔案與資料夾掃描工具

本工具為一個用於掃描指定目錄下所有檔案與資料夾資訊的小工具，並將掃描結果儲存成 CSV 檔。程式內建功能包含計算資料夾內所有檔案的大小、檔案數量，並展示檔案的名稱、大小、路徑、最後修改時間等資訊。

---

## 目錄

- [檔案與資料夾掃描工具](#檔案與資料夾掃描工具)
  - [目錄](#目錄)
  - [功能簡介](#功能簡介)
  - [專案資訊](#專案資訊)
  - [安裝與執行](#安裝與執行)
    - [環境需求](#環境需求)
    - [**建立虛擬環境**](#建立虛擬環境)
  - [打包成 EXE](#打包成-exe)
    - [**安裝 PyInstaller**](#安裝-pyinstaller)
    - [**打包成 EXE 檔案**](#打包成-exe-檔案)
  - [更新與使用 requirements.txt](#更新與使用-requirementstxt)
    - [**產生 requirements.txt**](#產生-requirementstxt)
    - [**安裝 requirements.txt**](#安裝-requirementstxt)
  - [程式架構說明](#程式架構說明)
    - [主要功能模組](#主要功能模組)
  - [CSV 輸出說明](#csv-輸出說明)
  - [注意事項](#注意事項)
  - [授權](#授權)

---

## 功能簡介

- **掃描目錄：** 自動遍歷指定目錄及其子目錄，獲取所有檔案與資料夾的資訊。
- **資料統計：** 計算資料夾內所有檔案的數量與總大小。
- **資訊展示：** 顯示檔案與資料夾的基本資訊，如名稱、類型、大小、路徑及最後修改時間。
- **CSV 輸出：** 將掃描結果儲存為 CSV 格式，方便進行後續處理或分析。

---

## 專案資訊

- **程式名稱：** 檔案與資料夾掃描工具
- **作者：** [CJhang](https://cjhang.com/)
- **版本：** 1.0.0 (2025/01/24)
- **描述：** 掃描指定目錄下的所有檔案與資料夾資訊，並將結果儲存成 CSV 檔。

---

## 安裝與執行

### 環境需求

- Python 3.x（建議使用 Python 3.6 以上版本）
- 標準 Python 套件：`os`、`csv`、`sys`、`datetime`

### **建立虛擬環境**

為了確保專案的環境一致性，建議使用虛擬環境。

1. 建立虛擬環境（僅需執行一次）：

   ```bash
   python -m venv venv
   ```

2. 啟動虛擬環境：

   - Windows：

     ```bash
     venv\Scripts\activate
     ```

   - macOS/Linux：

     ```bash
     source venv/bin/activate
     ```

3. 請先升級 pip：

    ```bash
    pip install --upgrade pip
    ```

4. 安裝相依套件：

   ```bash
   pip install -r requirements.txt
   ```

5. 執行程式：

   ```bash
   python ScanFilesFolders.py
   ```

6. 停用虛擬環境（可選）：

   ```bash
   deactivate
   ```

---

## 打包成 EXE

可以使用 `PyInstaller` 將此工具打包成 `.exe`，以便無需安裝 Python 即可執行。

### **安裝 PyInstaller**

```bash
pip install pyinstaller
```

### **打包成 EXE 檔案**

```bash
pyinstaller --onefile --console ScanFilesFolders.py
```

- `--onefile`：將程式打包成單一 EXE 檔案。
- `--console`：保留命令列視窗（若不希望顯示命令列，可改為 `--noconsole`）。

打包完成後，EXE 檔案會出現在 `dist/` 目錄內。

---

## 更新與使用 requirements.txt

`requirements.txt` 用於管理 Python 套件依賴，確保環境一致。

### **產生 requirements.txt**

```bash
pip freeze > requirements.txt
```

### **安裝 requirements.txt**

當其他使用者下載專案時，可執行以下指令來安裝所需的套件：

```bash
pip install -r requirements.txt
```

---

## 程式架構說明

### 主要功能模組

1. **程式資訊顯示 (`show_program_info`)**  
   顯示程式名稱、作者、版本與描述等基本資訊。

2. **掃描目錄 (`scan_directory`)**  
   遞迴遍歷指定目錄，並對每個項目呼叫 `process_directory` 或 `process_file` 進行處理。

3. **計算總數 (`count_total_items`)**  
   統計指定目錄下所有檔案與資料夾的數量，以便進度提示。

4. **資料夾處理 (`process_directory`)**  
   計算資料夾內檔案數量與總大小，並擷取基本資訊。

5. **檔案處理 (`process_file`)**  
   取得檔案名稱、大小、路徑及最後修改時間。

6. **CSV 儲存 (`save_to_csv`)**  
   將處理後的結果以 CSV 格式儲存。

---

## CSV 輸出說明

- **輸出檔名：**  
  掃描結果的 CSV 檔會以 `scan_results_YYYYMMDD_HHMMSS.csv` 命名。

- **CSV 欄位說明：**
  
  | 欄位名稱 | 說明 |
  |----------|------|
  | Type | 資料類型 (`File` 或 `Folder`) |
  | Name | 檔案或資料夾名稱 |
  | Extension | 附檔名（資料夾為 `None`） |
  | Size (bytes) | 檔案大小（資料夾為 `None`） |
  | Path | 檔案或資料夾完整路徑 |
  | File Count | 資料夾內檔案數量（檔案為 `None`） |
  | Total Size (bytes) | 資料夾內所有檔案的總大小（檔案為 `None`） |
  | Last Modified | 最後修改時間 |

---

## 注意事項

- **執行目錄：**
  程式會依據執行環境自動判斷當前目錄。
- **權限問題：**
  確保執行程式的目錄具有讀取權限，否則可能會因權限不足導致部分檔案無法讀取。
- **大資料夾掃描：**
  若目錄內檔案數量龐大，可能會耗費較長時間，請耐心等待。

---

## 授權

本程式碼採用 [MIT 授權條款](https://opensource.org/licenses/MIT) 發佈，歡迎各界在符合授權條款下進行修改與應用。
