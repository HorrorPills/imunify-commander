# menu.py
import os
import config

def show_menu():
    os.system('clear')
    print("")
    print("+-------------------------------------------+")
    print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
    print("+-------------------------------------------+")
    print("SCAN TOOLS")
    print("+-------------------------------------------+")
    print("Menu:")
    print("1. Scan Username")
    print("2. Scan Custom Path")
    print("3. Back to Main Menu")
    print("+-------------------------------------------+")
    choice = input("Choose number: ")
    
    if choice == "1":
        import scan_tools.scan_username as scan_username
        os.system('clear')
        scan_username.run_scan_menu()
    elif choice == "2":
        import scan_tools.scan_custom_path as scan_custom_path
        scan_custom_path.run_scan_menu()
    elif choice == "3":
        import main as main
        main.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")
        show_menu()

if __name__ == "__main__":
    show_menu()
