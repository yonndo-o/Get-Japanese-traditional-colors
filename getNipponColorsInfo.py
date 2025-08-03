import requests
import json

url = "https://nipponcolors.com/php/io.php"

# 讀取 colors.txt 裡的色名，每行一個
with open("colors.txt", "r", encoding="utf-8") as f:
    color_names = [line.strip() for line in f if line.strip()]

color_data = {}

# 遍歷每個色名並發送 API 請求
for i, name in enumerate(color_names, start=1):
    payload = {"color": name}
    try:
        response = requests.post(url, data=payload, timeout=5)
        data = response.json()
        color_data[name] = {
            "index": data.get("index"),
            "rgb": data.get("rgb"),
            "cmyk": data.get("cmyk")
        }
        print(f"{i:03}: {name} ✅")
    except Exception as e:
        print(f"{i:03}: {name} ❌ 錯誤：{e}")
        color_data[name] = {"error": str(e)}

# 儲存成 JSON 檔案
with open("nippon_colors_full.json", "w", encoding="utf-8") as f:
    json.dump(color_data, f, indent=2, ensure_ascii=False)

print("🎉 所有色彩資料已儲存成 nippon_colors_full.json")