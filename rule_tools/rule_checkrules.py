import subprocess
import re
from rule_tools.rules import disable_rule_for_account

def search_modsec_ids(ip_address):
    try:
        log_lines = subprocess.check_output(f"sudo grep modsec /var/log/imunify360/console.log | grep {ip_address}", shell=True)
        return log_lines.decode("utf-8").strip().split('\n')
    except subprocess.CalledProcessError:
        print("An error occurred while searching for ModSecurity IDs.")
        return []

def whitelist_modsec_rule(rule_id):
    try:
        subprocess.run(f"sudo imunify360-agent whitelist rule add {rule_id}", shell=True)
        print(f"Rule ID {rule_id} whitelisted successfully.")
    except subprocess.CalledProcessError:
        print(f"An error occurred while whitelisting Rule ID {rule_id}.")

def extract_info_blocks(log_lines):
    info_blocks = []
    timestamp_pattern = re.compile(r'\[(.*?)\]')
    rule_pattern = re.compile(r"'rule': '(.*?)'")
    ip_pattern = re.compile(r"'attackers_ip': '(.*?)'")
    domain_pattern = re.compile(r"'domain': '(.*?)'")
    message_pattern = re.compile(r"WAF: (.*?)'")
    info_start_pattern = re.compile(r"INFO\s+\[.*?\]")

    for log_line in log_lines:
        if info_start_pattern.match(log_line):
            timestamp = timestamp_pattern.search(log_line).group(1)
            rule = rule_pattern.search(log_line).group(1)
            attackers_ip_match = ip_pattern.search(log_line)
            attackers_ip = attackers_ip_match.group(1) if attackers_ip_match else "N/A"
            domain_match = domain_pattern.search(log_line)
            domain = domain_match.group(1) if domain_match else "N/A"
            message = message_pattern.search(log_line).group(1)
            info_blocks.append({
                'timestamp': timestamp,
                'rule': rule,
                'attackers_ip': attackers_ip,
                'domain': domain,
                'message': message
            })
    return info_blocks


def run_check_rules_menu():
    ip_address = input("Enter IP address: ")

    modsec_ids = search_modsec_ids(ip_address)
    info_blocks = extract_info_blocks(modsec_ids)

    print("+-------------------------------------------+")
    print(f"INFO Blocks for IP address {ip_address}")
    print("+-------------------------------------------+")

    if info_blocks:
        for block in info_blocks:
            print(f"Timestamp: {block['timestamp']}")
            print(f"Rule ID: {block['rule']}")
            print(f"Attacker's IP: {block['attackers_ip']}")
            print(f"Domain: {block['domain']}")  # Include domain here
            print(f"Message: {block['message']}")
            print("--------------------------------------------")
    else:
        print("No INFO Blocks found in logs for the specified IP address.")

    print("+-------------------------------------------+")
    print("Options:")
    print("2. Disable Rule by ID for an Account")
    print("3. Return to Main Menu")
    print("4. Exit")
    print("+-------------------------------------------+")
    choice = input("Choose number: ")

    if choice == "2":
        username = input("Enter username for the account: ")
        rule_id = input("Enter ModSecurity Rule ID to disable for the account: ")
        disable_rule_for_account(username, rule_id)
        run_check_rules_menu()  # Return to the options
    elif choice == "2":
        import main
        main.show_menu()
    elif choice == "3":
        print("Exiting IMUNIFY-COMMANDER. Goodbye!")
    else:
        print("Invalid choice. Please choose a valid option.")
        run_check_rules_menu()

if __name__ == "__main__":
    run_check_rules_menu()