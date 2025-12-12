# bulk_file_downloader.py
import requests

urls = [
    "https://example.com/file1.pdf",
    "https://example.com/file2.pdf"
]

for u in urls:
    filename = u.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(requests.get(u).content)
