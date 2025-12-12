# email_extractor.py
import re
import requests

url = "https://example.com/contact"
html = requests.get(url).text

emails = re.findall(r"[\\w\\.-]+@[\\w\\.-]+", html)
print(emails)
