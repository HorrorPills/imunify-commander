import subprocess
import os
import config
import time

SECONDS_IN_A_DAY = 24 * 60 * 60

def is_ip_in_blacklist(ip_address):
    try:
        output = subprocess.check_output(f"sudo imunify360-agent blacklist ip list --by-ip {ip_address} | grep {ip_address}", shell=True)
        return True if output else False
    except subprocess.CalledProcessError:
        return False

def get_whitelist_expiration(ip_address):
    try:
        output = subprocess.check_output(f"sudo imunify360-agent whitelist ip list --by-ip {ip_address} | grep {ip_address}", shell=True)
        expiration_seconds = int(output.strip().split()[4])
        expiration_days = expiration_seconds // SECONDS_IN_A_DAY
        return expiration_days
    except subprocess.CalledProcessError:
        return None

def run_check_ip_menu():
    while True:
        ip_address = input("Enter IP address (or 'q' to quit): ")
        print(f'Checking {ip_address}...')
        
        if ip_address.lower() == 'q':
            import ip_tools.ip_tools_menu as ip_tools_menu
            ip_tools_menu.show_menu()
        
        is_blacklisted = is_ip_in_blacklist(ip_address)
        is_whitelisted = is_ip_in_whitelist(ip_address)
        whitelist_expiration = get_whitelist_expiration(ip_address)
        
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
        if is_whitelisted and whitelist_expiration is not None:
            print(f"Expiration: {whitelist_expiration} days")
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
