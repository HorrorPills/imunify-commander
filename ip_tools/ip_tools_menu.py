# menu.py
import os

import config  # Import the VERSION variable from config.py

def show_menu():
    os.system('cls')
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
        import ip_status as ip_status
        ip_status.run_check_ip_menu()
    elif choice == "2":
        import rule_tools.rule_checkrules as rule_checkrules
        rule_checkrules.run_check_rules_menu()
    elif choice == "3":
        import main as main
        main.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")
        show_menu()

if __name__ == "__main__":
    show_menu()
