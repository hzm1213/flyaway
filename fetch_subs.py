import os
import requests
import hashlib

# 虚假节点
fake_node = "dm1lc3M6Ly9leUoySWpvaU1pSXNJbkJ6SWpvaVZHVnNaV2RvWVhKaGRHOXlMbkJvY0hKbGJuUnBZMnRsZEY5aFpHMXBiaUlzSW1GcFpDSTZJakUwT1RFMk1qZzNNaTFrTXpFMExUUTFOV1l0T1RFeE9TMWlNams0T1RRMU1tTXlOamdpTENKd2IzSjBJam9pTWpBd01URTRJaXdpYVdRaU9pSTJZelUxWldRNU5qVXRZbUkzT1MwME1Ea3lMVGt6TWpVdFpUSXlObVE0TXpBNU1XUXdJaXdpYm1WMElqb2lkM01pTENKMGVYQmxJam9pYm05dVpTSXNJbWh2YzNRaU9pSmxZMkZ1YVc1blpYSXVibUZ1YjNjdVkyOXRJaXdpZEd4eklqb2lkR3h6SW4wPQ"

# 获取所有订阅链接
subs = [v for k, v in os.environ.items() if k.startswith("SUBS_")]

# 输出目录
out_dir = "subs"
os.makedirs(out_dir, exist_ok=True)

def fetch_sub(url):
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        return r.text.strip()
    except:
        return fake_node

def file_changed(path, content):
    if not os.path.exists(path):
        return True
    with open(path, "r", encoding="utf-8") as f:
        old = f.read()
    return hashlib.md5(old.encode()).hexdigest() != hashlib.md5(content.encode()).hexdigest()

for i, url in enumerate(subs, 1):
    content = fetch_sub(url)
    file_path = os.path.join(out_dir, f"sub_{i}.txt")
    if file_changed(file_path, content):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {file_path}")
    else:
        print(f"No change: {file_path}")
