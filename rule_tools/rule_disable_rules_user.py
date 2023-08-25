import os
import config

def append_rules_to_file(file_path, rule_ids):
    for rule_id in rule_ids:
        command = f"echo 'SecRuleRemoveById {rule_id}' | sudo tee -a {file_path} > /dev/null"
        os.system(command)

def main():
    os.system('clear')
    print("")
    print("+-------------------------------------------+")
    print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
    print("+-------------------------------------------+")
    print("RULE TOOLS | DISABLE RULE ID")
    print("+-------------------------------------------+")
    username = input("Enter username: ")
    print("+-------------------------------------------+")
    rule_ids_input = input(f"Enter Rule ID's to disable for {username} (space-separated): ")
    print("+-------------------------------------------+")
    rule_ids = rule_ids_input.split()

    file_path = f'/usr/local/apache/conf/userdata/{username}/{username}.conf'

    if not os.path.exists(file_path):
        os.system(f"echo '<IfModule mod_security2.c>' | sudo tee {file_path} > /dev/null")
        os.system(f"echo '</IfModule>' | sudo tee -a {file_path} > /dev/null")

    append_rules_to_file(file_path, rule_ids)

    print("Rebuild httpd configuration?")
    print(" ")
    print("1. Yes")
    print("2. No")
    print("+-------------------------------------------+")
    rebuild_choice = input("Choose number: ")
    
    if rebuild_choice == "1":
        os.system('sudo /scripts/rebuildhttpdconf')
    elif rebuild_choice == "2":
        import rule_tools.rule_tools_menu as rule_tools_menu
        rule_tools_menu.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
