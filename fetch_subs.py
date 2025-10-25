import os
import requests
import hashlib

# 虚假节点
fake_node = "dm1lc3M6Ly9ldzBLSUNBaWRpSTZJQ0l5SWl3TkNpQWdJbkJ6SWpvZ0lseDFSRGd6UkZ4MVJFVkJRa1poYTJVZ1RtOWtaU0lzRFFvZ0lDSmhaR1FpT2lBaU1USTNMakF1TUM0eElpd05DaUFnSW5CdmNuUWlPaUFpT0RnNE1DSXNEUW9nSUNKcFpDSTZJQ0l3TldNMU1HTmhNaTAwWW1ReExUTm1OalV0WWpSalppMHlNR1k1TURCbVpqYzJZbVlpTEEwS0lDQWlZV2xrSWpvZ0lqSWlMQTBLSUNBaWMyTjVJam9nSW1GMWRHOGlMQTBLSUNBaWJtVjBJam9nSW5SamNDSXNEUW9nSUNKMGVYQmxJam9nSW01dmJtVWlMQTBLSUNBaWFHOXpkQ0k2SUNJaUxBMEtJQ0FpY0dGMGFDSTZJQ0lpTEEwS0lDQWlkR3h6SWpvZ0lpSXNEUW9nSUNKemJta2lPaUFpSWl3TkNpQWdJbUZzY0c0aU9pQWlJaXdOQ2lBZ0ltWndJam9nSWlJTkNuMD0NCg"

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
