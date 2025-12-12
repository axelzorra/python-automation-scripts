# website_uptime_monitor.py
import requests

url = "https://example.com"

try:
    requests.get(url, timeout=3)
    print("Website is ONLINE ✔")
except:
    print("Website is OFFLINE ❌")
