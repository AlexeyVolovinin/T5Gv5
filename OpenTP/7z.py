import requests

url = "https://7-zip.org/a/7z2501-x64.exe"
response = requests.get(url)

with open("7z2501-x64.exe", "wb") as file:
    file.write(response.content)