#!/usr/bin/env python3
import requests, json, sys, os, time

def banner():
    print("""
╔══════════════════════════════════════════════════════════╗
║ ███████╗██████╗ ██╗   ██╗ ██████╗ ███████╗███╗   ██╗    ║
║ ██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝ ██╔════╝████╗  ██║    ║
║ ███████╗██████╔╝ ╚████╔╝ ██║  ███╗█████╗  ██╔██╗ ██║    ║
║ ╚════██║██╔═══╝   ╚██╔╝  ██║   ██║██╔══╝  ██║╚██╗██║    ║
║ ███████║██║        ██║   ╚██████╔╝███████╗██║ ╚████║    ║
║ ╚══════╝╚═╝        ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ║
║                     v2.0 by sno0v                        ║
╚══════════════════════════════════════════════════════════╝
    """)

def ip_lookup():
    ip = input("\n[?] Masukkan IP Address: ")
    print("[*] Melacak...")
    
    try:
        # Multiple API untuk hasil maksimal
        apis = [
            f"http://ip-api.com/json/{ip}",
            f"https://ipinfo.io/{ip}/json",
            f"https://geolocation-db.com/json/{ip}"
        ]
        
        for api in apis:
            try:
                r = requests.get(api, timeout=5)
                data = r.json()
                
                print(f"\n{'='*50}")
                print(f"[+] HASIL DARI {api.split('/')[2]}")
                print('='*50)
                
                if 'query' in data or 'ip' in data:
                    print(f"IP Address    : {data.get('query') or data.get('ip')}")
                    print(f"Negara        : {data.get('country') or data.get('country_name')}")
                    print(f"Provinsi      : {data.get('regionName') or data.get('region')}")
                    print(f"Kota          : {data.get('city')}")
                    print(f"ZIP Code      : {data.get('zip')}")
                    print(f"Koordinat     : {data.get('lat')}, {data.get('lon')}")
                    print(f"ISP           : {data.get('isp') or data.get('org')}")
                    print(f"AS Number     : {data.get('as')}")
                    print(f"Zona Waktu    : {data.get('timezone')}")
                    
                if 'hostname' in data:
                    print(f"Hostname      : {data.get('hostname')}")
                    
                if 'anycast' in data:
                    print(f"Anycast       : {data.get('anycast')}")
                    
            except:
                continue
                
    except Exception as e:
        print(f"[-] Error: {e}")

def phone_tracker():
    print("\n[*] Fitur Phone Tracker")
    print("[!] Butuh API key dari:")
    print("    1. numverify.com (100 credit gratis)")
    print("    2. abstractapi.com (50/month gratis)")
    
    phone = input("\n[?] Nomor HP (contoh: 628123456789): ")
    api_key = input("[?] API Key (kosongkan untuk skip): ")
    
    if api_key:
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone}"
        r = requests.get(url)
        data = r.json()
        
        if data.get('valid'):
            print(f"\n[+] VALID: Ya")
            print(f"[+] Nomor: {data.get('international_format')}")
            print(f"[+] Prefix: {data.get('country_prefix')}")
            print(f"[+] Negara: {data.get('country_name')}")
            print(f"[+] Lokasi: {data.get('location')}")
            print(f"[+] Carrier: {data.get('carrier')}")
            print(f"[+] Tipe: {data.get('line_type')}")
        else:
            print("[-] Nomor tidak valid")
    else:
        print("[-] Masukkan API key untuk menggunakan fitur ini")

def username_search():
    username = input("\n[?] Username: ")
    
    sites = [
        ("Instagram", f"https://instagram.com/{username}"),
        ("Twitter/X", f"https://twitter.com/{username}"),
        ("Facebook", f"https://facebook.com/{username}"),
        ("GitHub", f"https://github.com/{username}"),
        ("YouTube", f"https://youtube.com/@{username}"),
        ("TikTok", f"https://tiktok.com/@{username}"),
        ("LinkedIn", f"https://linkedin.com/in/{username}"),
        ("Pinterest", f"https://pinterest.com/{username}"),
        ("Reddit", f"https://reddit.com/user/{username}"),
        ("Telegram", f"https://t.me/{username}"),
        ("Spotify", f"https://open.spotify.com/user/{username}"),
        ("Twitch", f"https://twitch.tv/{username}")
    ]
    
    print(f"\n[*] Mencari {username} di {len(sites)} platform...")
    time.sleep(1)
    
    print(f"\n{'='*60}")
    print(f"[+] HASIL PENCARIAN USERNAME: {username}")
    print('='*60)
    
    for name, url in sites:
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                print(f"[✓] {name:15} : ADA → {url}")
            elif r.status_code == 404:
                print(f"[✗] {name:15} : TIDAK ADA")
            else:
                print(f"[?] {name:15} : {r.status_code} → {url}")
        except:
            print(f"[!] {name:15} : ERROR")

def main():
    banner()
    
    while True:
        print("\n" + "═"*60)
        print(" MENU UTAMA SPYGEN77")
        print("═"*60)
        print("1. IP Lookup (Lengkap dengan ISP, Koordinat, dll)")
        print("2. Phone Tracker (Butuh API Key)")
        print("3. Username Search (12 Platform)")
        print("4. Exit")
        print("═"*60)
        
        choice = input("\n[>] Pilih menu (1-4): ")
        
        if choice == "1":
            ip_lookup()
        elif choice == "2":
            phone_tracker()
        elif choice == "3":
            username_search()
        elif choice == "4":
            print("\n[!] Keluar...")
            print("[+] Kunjungi repo: https://github.com/sno0v/SpyGen77")
            break
        else:
            print("[-] Pilihan tidak valid!")

if __name__ == "__main__":
    main()
