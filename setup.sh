#!/bin/bash
echo "Installing SZN-OTP Dependencies..."
pkg update && pkg upgrade -y
pkg install python git -y
pip install -r requirements.txt
echo "Setup Selesai! Ketik: python spammer.py"

