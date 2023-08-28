import subprocess
import os
import config
#import ip_tools_menu

def add_ip_to_blacklist(ip_address):
    subprocess.run(f"sudo imunify360-agent blacklist ip add {ip_address}", shell=True)

def remove_ip_from_blacklist(ip_address):
    subprocess.run(f"sudo imunify360-agent blacklist ip delete {ip_address}", shell=True)

def add_ip_to_whitelist(ip_address):
    subprocess.run(f"sudo imunify360-agent whitelist ip add {ip_address}", shell=True)

def remove_ip_from_whitelist(ip_address):
    subprocess.run(f"sudo imunify360-agent whitelist ip delete {ip_address}", shell=True)

def show_list_control_menu():
    while True:
        os.system('clear')
        print("+-------------------------------------------+")
        print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
        print("+-------------------------------------------+")
        print("MAIN MENU > IP TOOLS > CONTROL")
        print("+-------------------------------------------+")
        print("Menu:")
        print("1. Add IP to Whitelist/Blacklist")
        print("2. Remove IP from Whitelist/Blacklist")
        print("3. Back")
        print("+-------------------------------------------+")
        choice = input("Choose number: ")

        if choice == "1":
            ip_address = input("Enter IP address: ")
            print("Adding IP to:")
            print("1. Blacklist")
            print("2. Whitelist")
            print("+-------------------------------------------+")
            action_choice = input("Choose number: ")
            if action_choice == "1":
                add_ip_to_blacklist(ip_address)
            elif action_choice == "2":
                add_ip_to_whitelist(ip_address)
            else:
                print("Invalid choice. Please choose a valid option.")
        elif choice == "2":
            ip_address = input("Enter IP address: ")
            print("Removing IP from:")
            print("1. Blacklist")
            print("2. Whitelist")
            print("+-------------------------------------------+")
            action_choice = input("Choose number: ")
            if action_choice == "1":
                remove_ip_from_blacklist(ip_address)
            elif action_choice == "2":
                remove_ip_from_whitelist(ip_address)
            else:
                print("Invalid choice. Please choose a valid option.")
        elif choice == "3":
            import ip_tools.ip_tools_menu as ip_tools_menu
            ip_tools_menu.show_menu()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    show_list_control_menu()
