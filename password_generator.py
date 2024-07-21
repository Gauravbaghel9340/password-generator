import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = get_password_length()
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
