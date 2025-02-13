import os
import csv
import sys
from datetime import datetime

# 定義 CSV 欄位名稱常數，避免重複定義相同字面值
CSV_FIELDNAMES = [
    'Type',
    'Name',
    'Extension',
    'Size (bytes)',
    'Path',
    'File Count',
    'Total Size (bytes)',
    'Last Modified'
]

# 作者與程式資訊
__title__ = "檔案與資料夾掃描工具"
__author__ = "CJhang"
__version__ = "1.0.0 (2025/01/24)"
__description__ = "檔案與資料夾掃描工具"

def show_program_info():
    """顯示程式相關資訊"""
    print("=" * 50)
    print(f"程式名稱：{__title__}")
    print(f"作者：{__author__}")
    print(f"版本：{__version__}")
    print(f"描述：{__description__}")
    print("=" * 50)
    print()

def create_default_record():
    """
    根據 CSV_FIELDNAMES 建立一個預設記錄字典，
    所有欄位的初始值皆為 None。
    """
    return {field: None for field in CSV_FIELDNAMES}

def scan_directory(root_dir):
    results = []
    total_items = count_total_items(root_dir)
    current_count = 0

    for root, dirs, files in os.walk(root_dir):
        for directory in dirs:
            current_count += 1
            folder_path = os.path.join(root, directory)
            print(f"[{current_count}/{total_items}] 正在處理資料夾：{folder_path}")
            results.append(process_directory(folder_path, directory))

        for file in files:
            current_count += 1
            file_path = os.path.join(root, file)
            print(f"[{current_count}/{total_items}] 正在處理檔案：{file_path}")
            results.append(process_file(file_path, file))

    return results

def count_total_items(root_dir):
    total_items = 0
    for _, dirs, files in os.walk(root_dir):
        total_items += len(dirs) + len(files)
    return total_items

def process_directory(folder_path, directory):
    total_size = 0
    file_count = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
                file_count += 1
    last_modified = datetime.fromtimestamp(os.path.getmtime(folder_path)).strftime('%Y-%m-%d %H:%M:%S')
    
    # 利用輔助函式建立預設記錄，然後更新需要的欄位
    record = create_default_record()
    record.update({
        'Type': 'Folder',
        'Name': directory,
        'Path': folder_path,
        'File Count': file_count,
        'Total Size (bytes)': total_size,
        'Last Modified': last_modified
    })
    return record

def process_file(file_path, file):
    last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
    
    record = create_default_record()
    record.update({
        'Type': 'File',
        'Name': os.path.splitext(file)[0],
        'Extension': os.path.splitext(file)[1],
        'Size (bytes)': os.path.getsize(file_path),
        'Path': file_path,
        'Last Modified': last_modified
    })
    return record

def save_to_csv(data, output_file):
    # 使用 CSV_FIELDNAMES 常數來定義欄位名稱
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # 顯示程式資訊
    show_program_info()
    
    # 判斷當前執行的目錄（解決 _MEIxxxx 打包問題）
    if getattr(sys, 'frozen', False):
        current_dir = os.path.dirname(sys.executable)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))

    # 格式化當前時間為檔名的一部分
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_csv = os.path.join(current_dir, f'scan_results_{current_time}.csv')

    print(f"正在掃描資料夾：{current_dir}")
    # 執行掃描
    results = scan_directory(current_dir)

    # 儲存結果到 CSV
    save_to_csv(results, output_csv)

    # 顯示程式資訊
    show_program_info()

    print(f"掃描完成，結果已儲存到：{output_csv}")
    input("按下 Enter 鍵退出...")
