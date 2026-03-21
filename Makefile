# --- SZN-OTP AUTOMATION SYSTEM ---

install:
	@echo "[*] Installing dependencies..."
	@pkg install python nodejs git make clang -y
	@pip install -r requirements.txt
	@npm install
	@chmod +x setup.sh
	@./setup.sh

build:
	@echo "[*] Compiling Spammer.py to Binary..."
	@python compile.py build_ext --inplace
	@echo "[+] Success! Spammer.py is now encrypted."

run:
	@python Spammer.py

update:
	@git pull
	@echo "[+] Repository updated."

clean:
	@rm -rf build/ Spammer.c Spammer.pyc
	@echo "[*] Clean up finished."
