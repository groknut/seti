import re
import socket
from pathlib import Path

data_path = Path(__file__).parent.parent / "data" / "register.txt"
banned = {'urls': set(), 'domains': set(), 'ips': set()}

with open(data_path, encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        if len(parts) < 4:
            continue
        for key, val in zip(("urls", "domains", "ips"), parts[1:4]):
            banned[key] |= {x.strip().lower() for x in val.split(",") if x.strip()}

URL_PATTERN = re.compile(
    r"^https?://"  # http:// https://
    r"((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # Домен
    r"localhost|"  # Либо localhost
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # Либо IPv4-адрес
    r"(?::\d{1,5})?"  # Опциональный порт: :80, :8080
    r"(?:/?|[/?]\S+)$",  # Опциональный путь
    re.IGNORECASE,
)
url = input("Input url: ").strip().lower()

if url in banned["urls"]:
    print("BLOCKED: url")
    raise SystemExit

m = URL_PATTERN.match(url)
if not m:
    print("bad url"); raise SystemExit
domain = m.group(1)
if domain in banned["domains"]:
    print("BLOCKED: domain"); raise SystemExit

try:
    _, _, ips = socket.gethostbyname_ex(domain)
except socket.gaierror:
    ips = []
hit = next((ip for ip in ips if ip in banned["ips"]), None)
print(f"BLOCKED: ip {hit}" if hit else "OK")
