import random
import string

def generatePassword(pwlength, use_symbols, use_uppercase, use_lowercase, use_numbers):
    # Create the character pool based on user preferences
    alphabet = ""
    if use_lowercase:
        alphabet += string.ascii_lowercase
    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_numbers:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    passwords = []

    for _ in range(pwlength):
        password = "".join(random.choice(alphabet) for _ in range(pwlength))
        passwords.append(password)

    return passwords

def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")

    # Ask for password criteria
    use_symbols = input("Do you want to add symbols? (yes/no): ").strip().lower() == 'yes'
    use_uppercase = input("Do you want to add uppercase characters? (yes/no): ").strip().lower() == 'yes'
    use_lowercase = input("Do you want to add lowercase characters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Do you want to add numbers? (yes/no): ").strip().lower() == 'yes'
    
    # Ask for password length
    length = int(input("Enter the length of the passwords (minimum length should be 3): "))
    if length < 3:
        length = 3

    # Generate passwords
    passwords = generatePassword(length, use_symbols, use_uppercase, use_lowercase, use_numbers)

    # Print generated passwords
    for i in range(numPasswords):
        print("Password #" + str(i + 1) + " = " + passwords[i])

main()
