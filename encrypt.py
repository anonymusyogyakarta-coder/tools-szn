import os, base64

def obfuscate(file_name):
    try:
        with open(file_name, 'r') as f:
            data = f.read()
        
        # Proses Encrypt ke Base64 (Biar kodenya jadi huruf acak)
        b64_data = base64.b64encode(data.encode()).decode()
        
        # Header ala Sanz tapi versi Instagram kamu
        header = f'''#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
# Mau ngapain ngab? Tinggal pake aja!
# Script by SZN-V6 - INSTAGRAM: HZNXWICK
'''
        # Bagian ini yang bakal bikin ribuan kata HZNX
        body = f"HZNX = '{b64_data}'\n"
        body += "hznx = 'HZNX' * 1000 # Dummy data biar pusing\n"
        body += "exec(__import__('base64').b64decode(HZNX))"

        with open('Spammer_Enc.py', 'w') as f:
            f.write(header + body)
        
        print("[+] Berhasil! File 'Spammer_Enc.py' sudah jadi.")
    except Exception as e:
        print(f"[-] Error: {e}")

obfuscate('Spammer.py')
