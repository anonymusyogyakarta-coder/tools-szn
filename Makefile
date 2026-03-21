# --- SZN-OTP AUTOMATION SYSTEM V6 ---
# Dev: anonymusyogyakarta-coder

G = \033[1;32m
R = \033[1;31m
Y = \033[1;33m
B = \033[1;34m
N = \033[0m

install:
	@echo "$(B)[*] Sedang memperbarui sistem Termux...$(N)"
	@pkg update && pkg upgrade -y
	@echo "$(B)[*] Menginstall alat tempur (NodeJS, Python, C++)...$(N)"
	@pkg install python nodejs git make clang libcurl -y
	@echo "$(B)[*] Memasang modul Python (requirements)...$(N)"
	@pip install --upgrade pip
	@pip install -r requirements.txt
	@echo "$(B)[*] Memasang modul NodeJS (package.json)...$(N)"
	@npm install
	@chmod +x setup.sh
	@echo "$(G)[+] Semua bahan sudah siap!$(N)"

build:
	@echo "$(Y)[*] Mengunci kode (Compiling to Binary)...$(N)"
	@python compile.py build_ext --inplace
	@rm -rf build/ Spammer.c
	@echo "$(G)[+] Script berhasil di-encrypt! Anti-Copas aktif.$(N)"

run:
	@python Spammer.py

update:
	@echo "$(Y)[*] Menarik data terbaru dari GitHub...$(N)"
	@git pull
	@echo "$(G)[+] Berhasil diperbarui!$(N)"

clean:
	@rm -rf __pycache__ node_modules
	@echo "$(R)[!] Folder sampah dibersihkan.$(N)"
