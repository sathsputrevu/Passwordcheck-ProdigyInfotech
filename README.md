# Password Complexity Checker

## Overview
The Password Complexity Checker is a tool designed to evaluate the strength of user passwords and enhance online security. It provides real-time feedback on password strength and checks if passwords have been involved in any known data breaches using the HaveIBeenPwned API.

## Features
- **Password Strength Assessment**: Evaluates passwords based on length, uppercase and lowercase letters, numbers, and special characters.
- **Pwned Password Check**: Integrates with the HaveIBeenPwned API to identify commonly used and leaked passwords.
- **User Experience**: Offers secure password input with hidden characters and provides instant feedback.
- **Cross-Platform Compatibility**: Functions on both Windows and Unix-like systems.

## Technology Stack
- Python
- Hashing with SHA-1
- Integration with HaveIBeenPwned API
- Colorama for terminal color output

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.
- Access to the internet for the API calls.

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/password-complexity-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-complexity-checker
   ```
3. Install the required packages:
   ```bash
   pip install requests colorama
   ```

### Usage
1. Run the program:
   ```bash
   python pass.py
   ```
2. Follow the on-screen prompts to check your password.

## Example
```
Welcome to the Password Strength and Security Checker!
---------------------------------------------
1. Check a Password
2. Exit
---------------------------------------------
Choose an option (1 or 2): 1

Enter your password (input is hidden):
Password: ********
Password Strength: Weak
Password should be at least 12 characters long for higher security.
Password not found in any breaches.
Your password appears safe from known breaches.
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or enhancements.

## License
This project is licensed under the MIT License.
