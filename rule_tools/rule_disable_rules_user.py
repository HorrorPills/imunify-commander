import os
import config

def append_rules_to_file(file_path, rule_ids):
    # Prepare the content to append
    append_content = '\n'.join([f'SecRuleRemoveById {rule_id}' for rule_id in rule_ids])

    # Read the existing file content
    with open(file_path, 'r') as file:
        existing_content = file.read()

    # Modify the existing content to include the appended rules
    modified_content = existing_content.replace('</IfModule>', f'{append_content}\n</IfModule>')

    # Write the modified content back to the file using a shell command
    os.system(f"echo '{modified_content}' | sudo tee {file_path}")

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
    elif rebuild_choice == "2":
        import rule_tools.rule_tools_menu as rule_tools_menu
        rule_tools_menu.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
