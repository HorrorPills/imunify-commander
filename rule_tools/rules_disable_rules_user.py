import os

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
    username = input("Enter username: ")
    rule_ids_input = input("Enter Rule ID's to disable (space-separated): ")
    rule_ids = rule_ids_input.split()

    file_path = f'/usr/local/apache/conf/userdata/{username}/{username}.conf'

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write('<IfModule mod_security2.c>\n</IfModule>\n')

    append_rules_to_file(file_path, rule_ids)

    rebuild_config = input("Rebuild httpd configuration? (yes/no): ")
    if rebuild_config.lower() == 'yes':
        os.system('sudo /scripts/rebuildhttpdconf')

if __name__ == "__main__":
    main()
