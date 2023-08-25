import subprocess
import os
import ip_tools_menu

def add_ip_to_blacklist(ip_address):
    subprocess.run(f"sudo imunify360-agent blacklist ip add {ip_address}", shell=True)

def remove_ip_from_blacklist(ip_address):
    subprocess.run(f"sudo imunify360-agent blacklist ip delete {ip_address}", shell=True)

def add_ip_to_whitelist(ip_address):
    subprocess.run(f"sudo imunify360-agent whitelist ip add {ip_address}", shell=True)

def remove_ip_from_whitelist(ip_address):
    subprocess.run(f"sudo imunify360-agent whitelist ip delete {ip_address}", shell=True)

def show_list_control_menu():
    import ip_tools_menu  # Import locally to avoid circular import

    os.system('clear')
    ip_address = input("Enter IP address: ")
    while True:
        os.system('clear')
        print(f"Options for {ip_address}")
        print("+-------------------------------------------+")
        print("1. Add")
        print("2. Remove")
        print("3. Back")
        print("+-------------------------------------------+")
        choice = input("Choose number: ")

        if choice == "1":
            action = "add"
        elif choice == "2":
            action = "remove"
        elif choice == "3":
            ip_tools_menu.show_menu()  # Use the locally imported module
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            continue

        if action == "add":
            # ... (your existing code)
        elif action == "remove":
            # ... (your existing code)

if __name__ == "__main__":
    show_list_control_menu()