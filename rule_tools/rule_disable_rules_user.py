import os
import config

def append_rules_to_file(file_path, rule_ids):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        inside_block = False

        for line in lines:
            if line.strip() == '<IfModule mod_security2.c>':
                inside_block = True
                file.write(line)
            elif line.strip() == '</IfModule>':
                inside_block = False
                file.write('\n')  # Add a newline before appending new rules
                for rule_id in rule_ids:
                    file.write(f'SecRuleRemoveById {rule_id}\n')
                file.write(line)
            elif inside_block:
                file.write(line)
            else:
                file.write(line)

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

    if not os.system(f"sudo test -d {folder_path}"):
        os.system(f"sudo mkdir -p {folder_path}")
        os.system(f"sudo chmod 755 {folder_path}")
    
    if not os.path.exists(file_path):
        os.system(f"sudo sh -c 'echo \"<IfModule mod_security2.c>\" > {file_path}'")
        os.system(f"sudo sh -c 'echo \"</IfModule>\" >> {file_path}'")

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
