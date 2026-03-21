#!/bin/bash

# --- SZN SYSTEM HYBRID INSTALLER ---
echo -e "\e[1;34m[*] Memulai Setup SZN-OTP Ultimate...\e[0m"

# 1. Update & Install Core (Python + NodeJS)
echo -e "\e[1;33m[*] Installing Python & NodeJS...\e[0m"
pkg update && pkg upgrade -y
pkg install python nodejs git make -y

# 2. Install Bahan Python (requirements.txt)
echo -e "\e[1;33m[*] Installing Python Modules...\e[0m"
pip install --upgrade pip
pip install -r requirements.txt

# 3. Install Bahan NodeJS (package.json)
echo -e "\e[1;33m[*] Installing NodeJS Modules...\e[0m"
npm install

# 4. Beri Izin Eksekusi
chmod +x Spammer.py

echo -e "\e[1;32m\n[+] SETUP SELESAI!\e[0m"
echo -e "\e[1;32m[+] Ketik 'make run' atau 'python Spammer.py' untuk mulai.\e[0m"
