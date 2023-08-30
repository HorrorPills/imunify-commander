import subprocess
import os
import config
import time
from datetime import datetime

SECONDS_IN_A_DAY = 24 * 60 * 60

def is_ip_in_blacklist(ip_address):
    try:
        output = subprocess.check_output(f"sudo imunify360-agent blacklist ip list --by-ip {ip_address} | grep {ip_address}", shell=True)
        return True if output else False
    except subprocess.CalledProcessError:
        return False

def is_ip_in_whitelist(ip_address):
    try:
        output = subprocess.check_output(f"sudo imunify360-agent whitelist ip list | grep {ip_address}", shell=True)
        return True if output else False
    except subprocess.CalledProcessError:
        return False

def get_ip_expiration(ip_address):
    try:
        output = subprocess.check_output(f"sudo sqlite3 /var/imunify360/imunify360.db 'select * from iplist' | grep \"{ip_address}\"", shell=True)
        fields = output.split(b'|')
        if len(fields) >= 5:
            expiration_timestamp = int(fields[2])
            expiration_date = datetime.fromtimestamp(expiration_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            return expiration_timestamp, expiration_date
        else:
            return None, None
    except subprocess.CalledProcessError:
        return None, None

def run_check_ip_menu():
    while True:
        ip_address = input("Enter IP address (or 'q' to quit): ")
        print(f'Checking {ip_address}...')
        
        if ip_address.lower() == 'q':
            import ip_tools.ip_tools_menu as ip_tools_menu
            ip_tools_menu.show_menu()
        
        is_blacklisted = is_ip_in_blacklist(ip_address)
        is_whitelisted = is_ip_in_whitelist(ip_address)
        expiration_timestamp, expiration_date = get_ip_expiration(ip_address)
        
        if expiration_timestamp is not None:
            current_timestamp = int(time.time())
            days_until_expiration = max(0, (expiration_timestamp - current_timestamp) // SECONDS_IN_A_DAY)
            expiration_status = f"{days_until_expiration} days"
        else:
            expiration_status = "Not found"

        os.system('clear')
        print("")
        print("+-------------------------------------------+")
        print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
        print("+-------------------------------------------+")
        print("MAIN MENU > IP TOOLS > STATUS")
        print("+-------------------------------------------+")
        print(f"Status for {ip_address}")
        print("+-------------------------------------------+")
        print(f"Blacklist: {is_blacklisted}")
        print(f"Whitelist: {is_whitelisted}")
        print(f"Expiration: {expiration_status}")
        if expiration_date:
            print(f"Expiration Date: {expiration_date}")
        print("+-------------------------------------------+")
        print("1. Check Status of another IP Address")
        print("2. Back")
        print("+-------------------------------------------+")
        choice = input("Choose number: ")

        if choice == "1":
            continue
        elif choice == "2":
            import ip_tools.ip_tools_menu as ip_tools_menu
            ip_tools_menu.show_menu()
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    run_check_ip_menu()
