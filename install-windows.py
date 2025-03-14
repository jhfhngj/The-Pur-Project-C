import shutil

import requests

repo = requests.get("https://github.com/jhfhngj/The-Pur-Project-C.git")

print(repo.content)

main = "main.exe"

shutil.copy(main, "C:/Windows/pur.exe")
