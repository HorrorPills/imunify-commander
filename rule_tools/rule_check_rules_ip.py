import subprocess
import re
import config

def search_modsec_ids(ip_address):
    try:
        log_lines = subprocess.check_output(f"sudo grep -e 'modsec' -e 'INFO BLOCK' /var/log/imunify360/console.log | grep {ip_address}", shell=True)
        return log_lines.decode("utf-8").strip().split('\n')
    except subprocess.CalledProcessError:
        print("An error occurred while searching for ModSecurity IDs.")
        return []

def extract_info_blocks(log_lines):
    info_blocks = []
    timestamp_pattern = re.compile(r'\[(.*?)\]')
    rule_pattern = re.compile(r"'rule': '(.*?)'")
    ip_pattern = re.compile(r"'attackers_ip': '(.*?)'")
    domain_pattern = re.compile(r"'domain': '(.*?)'")
    message_pattern = re.compile(r"WAF: (.*?)'")
    name_pattern = re.compile(r"'name': '(.*?)'")  # Add name pattern
    info_start_pattern = re.compile(r"INFO\s+\[.*?\]")

    for log_line in log_lines:
        if info_start_pattern.match(log_line):
            timestamp = timestamp_pattern.search(log_line).group(1)
            rule = rule_pattern.search(log_line).group(1)
            attackers_ip_match = ip_pattern.search(log_line)
            attackers_ip = attackers_ip_match.group(1) if attackers_ip_match else "N/A"
            domain_match = domain_pattern.search(log_line)
            domain = domain_match.group(1) if domain_match else "N/A"
            message_match = message_pattern.search(log_line)
            message = message_match.group(1) if message_match else "N/A"
            name_match = name_pattern.search(log_line)  # Extract 'name'
            name = name_match.group(1) if name_match else "N/A"
            info_blocks.append({
                'timestamp': timestamp,
                'rule': rule,
                'attackers_ip': attackers_ip,
                'domain': domain,
                'message': message,
                'name': name  # Add 'name' to the dictionary
            })
    return info_blocks

def run_check_rules_menu():
    print("")
    print("+-------------------------------------------+")
    print(f"IMUNIFY-COMMANDER {config.VERSION} | WEBD.pl")
    print("+-------------------------------------------+")
    print("MAIN MENU > RULE TOOLS > LOOKUP RULES")
    print("+-------------------------------------------+")
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
            print(f"Domain: {block['domain']}")
            print(f"Message: {block['message']}")
            print(f"Name: {block['name']}")
            print("--------------------------------------------")
    else:
        print("No INFO Blocks found in logs for the specified IP address.")

    print("+-------------------------------------------+")
    print("Options:")
    print("1. Back")
    print("+-------------------------------------------+")
    choice = input("Choose number: ")

    if choice == "1":
        import rule_tools.rule_tools_menu as rule_tools_menu
        rule_tools_menu.show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")
        run_check_rules_menu()

if __name__ == "__main__":
    run_check_rules_menu()
