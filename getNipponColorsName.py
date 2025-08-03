import requests
from bs4 import BeautifulSoup

url = "https://nipponcolors.com"
headers = {"User-Agent": "Mozilla/5.0"}

# 發送 GET 請求抓取 HTML
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 找出所有 a 標籤的文字
color_elements = soup.select("nav#colorContainer ul#colors li div a")
color_names = [a.text.strip() for a in color_elements]

# 建立 txt 檔案並儲存第二部分的色彩名稱
with open("colors.txt", "w", encoding="utf-8") as f:
    for i, name in enumerate(color_names, start=1):
        print(f"{i:03}: {name}")
        try:
            # 擷取逗號後的中文色彩名稱（第2部分）
            short_name = name.split(',')[1].strip()
            f.write(short_name + "\n")
        except IndexError:
            print(f"⚠️ 第 {i:03} 筆資料格式異常：{name}")
            continue

print("✅ 所有色彩名稱已寫入 colors.txt")