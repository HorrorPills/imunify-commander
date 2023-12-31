import os
import config
import re

def append_rules_to_file(file_path, rule_ids):
    append_content = '\n'.join([f'SecRuleRemoveById {rule_id}' for rule_id in rule_ids])
    append_content_escaped = re.escape(append_content)  # Escape special characters

    # Use 'sed' to replace content within the </IfModule> tag.
    os.system(f"sudo sed -i '/<IfModule mod_security2.c>/,/<\\/IfModule>/ s/<\\/IfModule>/{append_content_escaped}\\n<\\/IfModule>/' {file_path}")

def main():
    os.system('clear')
    print("")
    print("+-------------------------------------------+")
    print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
    print("+-------------------------------------------+")
    print("MAIN MENU > RULE TOOLS > DISABLE RULE ID")
    print("+-------------------------------------------+")
    username = input("Enter username: ")
    print("+-------------------------------------------+")
    rule_ids_input = input(f"Enter Rule ID's to disable for {username} (space-separated): ")
    print("+-------------------------------------------+")
    rule_ids = rule_ids_input.split()

    folder_path = f'/usr/local/apache/conf/userdata/{username}'
    file_path = f'{folder_path}/{username}.conf'

    if not os.path.exists(folder_path):
        os.system(f"sudo mkdir -p {folder_path}")
        os.system(f"sudo chmod 755 {folder_path}")

    if not os.path.exists(file_path):
        os.system(f"echo '<IfModule mod_security2.c>\n</IfModule>\n' | sudo tee {file_path}")

    append_rules_to_file(file_path, rule_ids)

    print("+-------------------------------------------+")
    print("Rebuild httpd configuration?")
    print(" ")
    print("1. Yes")
    print("2. No")
    print("+-------------------------------------------+")
    rebuild_choice = input("Choose number: ")
    
    if rebuild_choice == "1":
        os.system('sudo /scripts/rebuildhttpdconf')
        print("[OK] Rebuilt httpd.conf")
    if rebuild_choice == "yes":
        os.system('sudo /scripts/rebuildhttpdconf')
        print("[OK] Rebuilt httpd.conf")
    elif rebuild_choice == "2":
        import rule_tools.rule_tools_menu as rule_tools_menu
        rule_tools_menu.show_menu()
    elif rebuild_choice == "no":
        import rule_tools.rule_tools_menu as rule_tools_menu
        rule_tools_menu.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
