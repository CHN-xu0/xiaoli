import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "Safari/537.36 Edg/110.0.1587.57"
}
response = requests.get("https://movie.douban.com/top250", headers=headers)
print(response.text)
