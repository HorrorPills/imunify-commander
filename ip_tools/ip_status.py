import subprocess
import os

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

def run_check_ip_menu():
    while True:
        ip_address = input("Enter IP address (or 'q' to quit): ")
        
        if ip_address.lower() == 'q':
            ip_tools.ip_tools_menu.show_menu()
        
        is_blacklisted = is_ip_in_blacklist(ip_address)
        is_whitelisted = is_ip_in_whitelist(ip_address)
        
        os.system('clear')
        print("+-------------------------------------------+")
        print(f"Status for {ip_address}")
        print("+-------------------------------------------+")
        print(f"Blacklist: {is_blacklisted}")
        print(f"Whitelist: {is_whitelisted}")
        print("+-------------------------------------------+")
        print("1. Check Status of another IP Address")
        print("2. Back")
        print("+-------------------------------------------+")
        choice = input("Choose number: ")

        if choice == "1":
            print(f'Checking {ip_address}...')
            continue
        elif choice == "2":
            import ip_tools_menu as ip_tools_menu
            ip_tools.ip_tools_menu.show_menu()
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    run_check_ip_menu()