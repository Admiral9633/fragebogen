"""
Diagnose-Skript – direkt auf dem SAMAS-Laptop ausführen
Zeigt den genauen HTTP-Response des Servers
"""
import configparser
from pathlib import Path
import requests

CONFIG_FILE = Path(__file__).parent / "config.ini"
cfg = configparser.ConfigParser()
cfg.read(str(CONFIG_FILE), encoding="utf-8")
s = cfg["bridge"]

api_url = s["api_url"].rstrip("/")
api_key = s["api_key"]

print(f"API-URL : {api_url}")
print(f"API-Key : {api_key}")
print(f"Ziel    : {api_url}/gdt/session/")
print("-" * 60)

# Test 1: GET auf /api/ – prüft ob Server erreichbar
try:
    r = requests.get(f"{api_url}/session/00000000-0000-0000-0000-000000000000/", timeout=5)
    print(f"Server erreichbar: HTTP {r.status_code} ✓")
except Exception as e:
    print(f"Server NICHT erreichbar: {e}")
    exit(1)

print()

# Test 2: POST auf /api/gdt/session/ ohne Auth
r = requests.post(f"{api_url}/gdt/session/", json={}, timeout=5)
print(f"POST ohne Auth : HTTP {r.status_code}")
print(f"Response       : {r.text[:200]}")
print()

# Test 3: POST auf /api/gdt/session/ mit Auth
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
payload = {
    "patient_last_name":  "Test",
    "patient_first_name": "Diagnose",
    "patient_birth_date": "1980-01-01",
    "gdt_patient_id":     "DIAG-001",
}
r = requests.post(f"{api_url}/gdt/session/", json=payload, headers=headers, timeout=5)
print(f"POST mit Auth  : HTTP {r.status_code}")
print(f"Response       : {r.text[:500]}")
