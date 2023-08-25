# ip_tools_menu.py
import os
import config
import ip_tools.ip_status as ip_status
import ip_tools.ip_list_control as ip_list_control
import main as main

def show_menu():
    os.system('clear')
    print("")
    print("+-------------------------------------------+")
    print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
    print("+-------------------------------------------+")
    print("IP TOOLS")
    print("+-------------------------------------------+")
    print("Menu:")
    print("1. Whitelist/Blacklist Status")
    print("2. Whitelist/Blacklist Control")
    print("3. Back to Main Menu")
    print("+-------------------------------------------+")
    choice = input("Choose number: ")
    
    if choice == "1":
        ip_status.run_check_ip_menu()
    elif choice == "2":
        ip_list_control.show_list_control_menu()  # Call the function, not the module
    elif choice == "3":
        main.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")
        show_menu()

if __name__ == "__main__":
    show_menu()
