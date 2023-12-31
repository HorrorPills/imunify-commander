# menu.py
import os
import config

def show_menu():
    os.system('clear')
    print("")
    print("+-------------------------------------------+")
    print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
    print("+-------------------------------------------+")
    print("MAIN MENU > RULE TOOLS")
    print("+-------------------------------------------+")
    print("Menu:")
    print("1. Check Rules for IP")
    print("2. Disable Rule by ID for a User")
    print("3. Back to Main Menu")
    print("+-------------------------------------------+")
    choice = input("Choose number: ")
    
    if choice == "1":
        import rule_tools.rule_check_rules_ip as rule_check_rules_ip
        os.system('clear')
        rule_check_rules_ip.run_check_rules_menu()
    elif choice == "2":
        import rule_tools.rule_disable_rules_user as disable_rules_user
        disable_rules_user.main()
    elif choice == "3":
        import main as main
        main.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")
        show_menu()

if __name__ == "__main__":
    show_menu()
