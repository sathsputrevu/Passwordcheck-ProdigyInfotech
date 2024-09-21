import re
import hashlib
import sys
import requests
import platform

is_windows = platform.system() == "Windows"
if is_windows:
    import msvcrt
else:
    import termios
    import tty

from colorama import Fore, Style, init
init(autoreset=True)

HIBP_API_URL = "https://api.pwnedpasswords.com/range/"
COMMON_PASSWORDS = ["123456", "password", "qwerty", "abc123", "letmein", "admin"]

def check_password_pwned(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    
    response = requests.get(HIBP_API_URL + prefix)
    if response.status_code != 200:
        return False, f"{Fore.RED}Error checking HaveIBeenPwned API."
    
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return True, f"{Fore.RED}Password found in data breach {count} times. Avoid using this password."
    
    return False, f"{Fore.GREEN}Password not found in any breaches."

def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    else:
        feedback.append(f"{Fore.YELLOW}Password should be at least 12 characters long for higher security.")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append(f"{Fore.YELLOW}Password should contain at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(f"{Fore.YELLOW}Password should contain at least one lowercase letter.")
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append(f"{Fore.YELLOW}Password should contain at least one digit.")
    
    if re.search(r'[@$!%*#?&]', password):
        score += 1
    else:
        feedback.append(f"{Fore.YELLOW}Password should contain at least one special character.")
    
    if password.lower() in COMMON_PASSWORDS:
        feedback.append(f"{Fore.RED}This is a commonly used password. Avoid using easy-to-guess passwords.")
    
    if score >= 6:
        strength = f"{Fore.GREEN}{Style.BRIGHT}Very Strong"
    elif score == 5:
        strength = f"{Fore.GREEN}Strong"
    elif score == 4:
        strength = f"{Fore.YELLOW}Medium"
    else:
        strength = f"{Fore.RED}Weak"
    
    if not feedback:
        feedback.append(f"{Fore.GREEN}Password is strong and secure!")
    
    return strength, feedback

def get_password():
    password = ""
    sys.stdout.write(f"{Fore.CYAN}Password: ")
    sys.stdout.flush()
    
    if is_windows:
        while True:
            ch = msvcrt.getch()
            if ch == b'\r':
                sys.stdout.write("\n")
                break
            elif ch == b'\x08':
                if len(password) > 0:
                    password = password[:-1]
                    sys.stdout.write("\b \b")
            else:
                password += ch.decode('utf-8')
                sys.stdout.write('*')
            sys.stdout.flush()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                ch = sys.stdin.read(1)
                if ch == '\n':
                    sys.stdout.write("\n")
                    break
                elif ch == '\x7f':
                    if len(password) > 0:
                        password = password[:-1]
                        sys.stdout.write("\b \b")
                else:
                    password += ch
                    sys.stdout.write('*')
                sys.stdout.flush()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return password

def main():
    while True:
        print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to the Password Strength and Security Checker!")
        print(f"{Fore.CYAN}---------------------------------------------")
        print(f"{Fore.GREEN}1. Check a Password")
        print(f"{Fore.RED}2. Exit")
        print(f"{Fore.CYAN}---------------------------------------------")
        
        choice = input(f"{Fore.YELLOW}Choose an option (1 or 2): ")
        
        if choice == '1':
            print(f"\n{Fore.CYAN}{Style.BRIGHT}Enter your password (input is hidden):")
            password = get_password()
            strength, feedback = password_strength(password)
            print(f"\n{Fore.CYAN}Password Strength: {strength}")
            for comment in feedback:
                print(comment)
            pwned, pwned_feedback = check_password_pwned(password)
            print(f"\n{Fore.CYAN}Pwned Password Check:")
            print(pwned_feedback)
            if not pwned:
                print(f"{Fore.GREEN}Your password appears safe from known breaches.")
            print(f"{Fore.CYAN}You entered: {password}")
            input(f"\n{Fore.YELLOW}Press Enter to return to the main menu...")
        
        elif choice == '2':
            print(f"{Fore.GREEN}Exiting... Thank you for using the Password Checker!")
            break
        
        else:
            print(f"{Fore.RED}Invalid option! Please choose 1 or 2.\n")

if __name__ == "__main__":
    main()
