import marshal
import base64

def encode_and_save(filename):
    with open(filename, 'r') as file:
        script = file.read()

    try:
        compiled_code = compile(script, '<string>', 'exec')
        encoded_data = marshal.dumps(compiled_code)
        encoded_str = repr(encoded_data)

        result = f"import marshal\nexec(marshal.loads(b{encoded_str}))"

        with open('encoded_data.py', 'w') as file:
            file.write(result)

        print("Encoding completed! Result saved in 'encoded_data.py'")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to encode. Returning to the main menu.")

def load_and_decode(filename):
    try:
        with open(filename, 'r') as file:
            encoded_str = file.read()

        # Extract the binary data from the encoded string
        encoded_data_str = encoded_str.split('b')[-1].strip()
        encoded_data = eval(encoded_data_str)

        compiled_code = marshal.loads(encoded_data)

        return compiled_code
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to decode. Returning to the main menu.")

def main_menu():
    print("===== Main Menu =====")
    print("1. Encode Python File")
    print("2. Decode Marshal Script")
    print("0. Exit")

def encode_menu():
    filename = input("Enter the filename of the Python file to encode: ")
    encode_and_save(filename)

    while True:
        print("1. Main Menu")
        print("2. Back")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            main()
        elif choice == '2':
            return
        elif choice == '3':
            print("Thanks for using the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")

def decode_menu():
    filename = input("Enter the filename of the encoded data: ")

    decoded_code = load_and_decode(filename)

    if decoded_code is not None:
        print("Decoding completed! Decoded code:")
        print(decoded_code)

    while True:
        print("1. Main Menu")
        print("2. Back")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            main()
        elif choice == '2':
            return
        elif choice == '3':
            print("Thanks for using the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            encode_menu()
        elif choice == '2':
            decode_menu()
        elif choice == '0':
            print("Thanks for using the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# Example usage:
main()
