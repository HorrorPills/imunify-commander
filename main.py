# menu.py
import os
import config

def show_menu():
    os.system('clear')
    print("")
    print("+-------------------------------------------+")
    print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
    print("+-------------------------------------------+")
    print("MAIN MENU")
    print("+-------------------------------------------+")
    print("Menu:")
    print("1. IP Tools")
    print("2. Rule Tools")
    print("3. Scan Tools")
    print("4. Exit")
    print("+-------------------------------------------+")
    choice = input("Choose number: ")
    
    if choice == "1":
        import ip_tools.ip_tools_menu as ip_tools_menu
        ip_tools_menu.show_menu()
    elif choice == "2":
        import rule_tools.rule_tools_menu as rule_tools_menu
        rule_tools_menu.show_menu()
    elif choice == "3":
        import scan_tools.scan_tools_menu as scan_tools_menu
        scan_tools_menu.show_menu()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please choose a valid option.")
        input("Press Enter to continue...")
        show_menu()

if __name__ == "__main__":
    show_menu()
