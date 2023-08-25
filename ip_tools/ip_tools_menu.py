# menu.py
import os
import config

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
        import ip_tools.ip_status as ip_status
        ip_status.run_check_ip_menu()
    elif choice == "2":
        import ip_tools.ip_list_control as ip_list_control
        ip_list_control.show_list_control_menu()
    elif choice == "3":
        import main as main
        main.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")
        show_menu()

if __name__ == "__main__":
    show_menu()
