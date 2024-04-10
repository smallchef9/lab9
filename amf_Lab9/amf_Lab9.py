def encode(password):
    encoded_password = []
    for i in password:
        encChar = int(i)+3
        if encChar >= 10:
            encChar -= 10
        encoded_password.append(encChar)
    return encoded_password

def menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

def main():
    while True:
        menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        if choice == 3:
            break
        if choice == 2:


if __name__ == "__main__":
    main()