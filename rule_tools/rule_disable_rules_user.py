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

    file_path = f'/usr/local/apache/conf/userdata/{username}/{username}.conf'

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write('<IfModule mod_security2.c>\n</IfModule>\n')

    append_rules_to_file(file_path, rule_ids)

    print("+-------------------------------------------+")
    print("Rebuild httpd configuration?")
    print("1. Yes")
    print("2. No")
    print("+-------------------------------------------+")
    rebuild_choice = input("Choose number: ")
    
    if rebuild_choice == "1":
        os.system('sudo /scripts/rebuildhttpdconf')
    elif rebuild_choice == "2":
        print("Skipping httpd configuration rebuild.")
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
