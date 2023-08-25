# scan.py

import subprocess
import config  # Import the VERSION variable from config.py

def start_malware_scan(username):
    try:
        subprocess.run(f"sudo imunify360-agent malware on-demand start --path /home/{username}/public_html/", shell=True)
        print("Malware scan started successfully.")
    except subprocess.CalledProcessError:
        print("An error occurred while starting the malware scan.")

def run_scan_menu():
    print("")
    print("+-------------------------------------------+")
    username = input("Enter Username: ")
    start_malware_scan(username)

    print("+-------------------------------------------+")
    print("Options:")
    print("1. Return to Main Menu")
    print("2. Exit")
    print("+-------------------------------------------+")
    choice = input("Choose number: ")

    if choice == "1":
        import main
        main.show_menu()
    elif choice == "2":
        print("Exiting IMUNIFY-COMMANDER. Goodbye!")
    else:
        print("Invalid choice. Please choose a valid option.")
        run_scan_menu()

if __name__ == "__main__":
    run_scan_menu()
