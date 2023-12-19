import hashlib
import base64
import marshal
import os
import sys
import time

# colors
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
cyan = '\033[96m'
reset = '\033[0m'

# banner Code
def banner():
    os.system("clear")
    os.system("clear")
    print("\033[91m")
    print("        //  //")
    print("     ==//==//==\033[92m ┌  ┐┌──┐┌──┐┌  ┐     ┌──┐┌──┐┌──┐")
    print("      //  //\033[92m    ├──┤├──┤└──┐├──┤┌───┐│ ─┐├┤  │  │")
    print("   ==//==//==\033[92m   └  ┘└  ┘└──┘└  ┘└───┘└──┘└──┘└  ┘")
    print("    //  // \033[93m v 1.0")
    print("\033[0m")
    print("\033[93m                     <===[["+red+" coded by"+cyan+" AN9ND_XD "+reset+"\033[93m]===>\n"+reset)
    print("\033[93m                  <---("+red+" AN9ND <3 - Turbo Hackers >:) "+cyan+")--->\n"+reset)

# gen code
def gen():
    banner()
    print(red + " [ " + green + "Selected : Hashing {SHA256,MD5}" + red + " ]" + reset)
    print(" ")

    # ... (other parts of your gen function)

    print(yellow + "\t\t\t      [" + green + "4" + yellow + "]➟ " + green + "Marshal Encoder/Decoder" + reset)
    print(yellow + "\t\t\t      [" + green + "0" + yellow + "]➟ " + green + "Exit" + reset)

    try:
        gen_choice = int(input(green + "\nSelect option : " + reset))
        if gen_choice == 4:
            marshal_operations()
    except ValueError:
        print(red + "Error: Please enter a valid option (numeric value)." + reset)

    # ... (other parts of your gen function)

# verifier code
def verifier():
    banner()
    print(red + " [ " + green + "Selected : Verifier {SHA256,MD5}" + red + " ]" + reset)
    print(" ")

    # ... (other parts of your verifier function)

    print(yellow + "\t\t\t      [" + green + "4" + yellow + "]➟ " + green + "Marshal Encoder/Decoder" + reset)
    print(yellow + "\t\t\t      [" + green + "0" + yellow + "]➟ " + green + "Exit" + reset)

    try:
        verifier_choice = int(input(green + "\nSelect option : " + reset))
        if verifier_choice == 4:
            marshal_operations()
    except ValueError:
        print(red + "Error: Please enter a valid option (numeric value)." + reset)

    # ... (other parts of your verifier function)

# base64 code
def base64_gen():
    banner()
    print(red + " [ " + green + "Selected : Base64 Encoder/Decoder" + red + " ]" + reset)
    print(" ")

    # ... (other parts of your base64_gen function)

    print(yellow + "\t\t\t      [" + green + "4" + yellow + "]➟ " + green + "Marshal Encoder/Decoder" + reset)
    print(yellow + "\t\t\t      [" + green + "0" + yellow + "]➟ " + green + "Exit" + reset)

    try:
        base_gen_choice = int(input(green + "\nSelect option : " + reset))
        if base_gen_choice == 4:
            marshal_operations()
    except ValueError:
        print(red + "Error: Please enter a valid option (numeric value)." + reset)

    # ... (other parts of your base64_gen function)

# marshal code
def marshal_encode(data, file_path):
    try:
        with open(file_path, "wb") as f:
            marshal.dump(data, f)
        print(f"Object encoded using marshal and saved to {file_path}")
    except Exception as e:
        print(f"Error encoding object using marshal: {e}")

def marshal_decode(file_path):
    try:
        with open(file_path, "rb") as f:
            data = marshal.load(f)
            print("Object decoded using marshal:", data)
            return data
    except Exception as e:
        print(f"Error decoding object using marshal: {e}")

def marshal_operations():
    banner()
    print(red + " [ " + green + "Selected : Marshal Encoder/Decoder" + red + " ]" + reset)
    print(" ")

    # ... (other parts of your marshal_operations function)

    def marshal_encode_operation():
        banner()
        print(red + " [ " + green + "Selected : Marshal Encoder" + red + " ]" + reset)
        print(" ")
        data_to_encode = input(green + "Enter the data to encode using marshal:\n : " + reset)
        file_path = input(green + "\nEnter the file path to save the encoded data:\n : " + reset)

        try:
            python_object = eval(data_to_encode)
            marshal_encode(python_object, file_path)
        except Exception as e:
            print(cyan + "\nError converting input data to Python object: " + str(e) + reset)

        print(yellow + "\n\t\t[" + green + "1" + yellow + "]➟ " + green + "Main Menu" + reset)
        print(yellow + "\t\t[" + green + "2" + yellow + "]➟ " + green + "Back" + reset)
        print(yellow + "\t\t[" + green + "0" + yellow + "]➟ " + green + "Exit" + reset)

        try:
            back_choice = int(input(green + "\nSelect Option : " + reset))
            if back_choice == 1:
                main()
            if back_choice == 2:
                marshal_operations()
            elif back_choice == 0:
                print(cyan + "\nThanks For Using This Program" + reset)
            else:
                print(cyan + "\n Wrong Input ! , Try again" + reset)
                time.sleep(2)
                marshal_encode_operation()
        except ValueError:
            print(red + "Error: Please enter a valid option (numeric value)." + reset)

    def marshal_decode_operation():
        banner()
        print(red + " [ " + green + "Selected : Marshal Decoder" + red + " ]" + reset)
        print(" ")
        file_path = input(green + "Enter the file path with the encoded data using marshal:\n : " + reset)

        try:
            decoded_data = marshal_decode(file_path)
        except Exception as e:
            print(cyan + "\nError decoding data using marshal: " + str(e) + reset)

        print(yellow + "\n\t\t[" + green + "1" + yellow + "]➟ " + green + "Main Menu" + reset)
        print(yellow + "\t\t[" + green + "2" + yellow + "]➟ " + green + "Back" + reset)
        print(yellow + "\t\t[" + green + "0" + yellow + "]➟ " + green + "Exit" + reset)

        try:
            back_choice = int(input(green + "\nSelect Option : " + reset))
            if back_choice == 1:
                main()
            if back_choice == 2:
                marshal_operations()
            elif back_choice == 0:
                print(cyan + "\nThanks For Using This Program" + reset)
            else:
                print(cyan + "\n Wrong Input ! , Try again" + reset)
                time.sleep(2)
                marshal_decode_operation()
        except ValueError:
            print(red + "Error: Please enter a valid option (numeric value)." + reset)

    print(yellow + "\t\t\t      [" + green + "1" + yellow + "]➟ " + green + "Marshal Encode" + reset)
    print(yellow + "\t\t\t      [" + green + "2" + yellow + "]➟ " + green + "Marshal Decode" + reset)
    print(yellow + "\t\t\t      [" + green + "3" + yellow + "]➟ " + green + "Back" + reset)
    print(yellow + "\t\t\t      [" + green + "0" + yellow + "]➟ " + green + "Exit" + reset)

    try:
        marshal_choice = int(input(green + "\nSelect option : " + reset))
        if marshal_choice == 1:
            marshal_encode_operation()
        elif marshal_choice == 2:
            marshal_decode_operation()
        elif marshal_choice == 3:
            main()
        elif marshal_choice == 0:
            print(cyan + "\nThanks For Using This Program" + reset)
        else:
            print(cyan + "\n Wrong Input ! , Try again" + reset)
            time.sleep(2)
            marshal_operations()
    except ValueError:
        print(red + "Error: Please enter a valid option (numeric value)." + reset)

# main code
def main():
    try:
        banner()
        print(yellow + "\t\t\t      [" + green + "1" + yellow + "]➟ " + green + "Generate Hash" + reset)
        print(yellow + "\t\t\t      [" + green + "2" + yellow + "]➟ " + green + "Verify Hash" + reset)
        print(yellow + "\t\t\t      [" + green + "3" + yellow + "]➟ " + green + "Base64 Encoder/Decoder" + reset)
        print(yellow + "\t\t\t      [" + green + "4" + yellow + "]➟ " + green + "Marshal Encoder/Decoder" + reset)
        print(yellow + "\t\t\t      [" + green + "0" + yellow + "]➟ " + green + "Exit" + reset)

        try:
            choice = int(input(green + "\nSelect option : " + reset))
            if choice == 1:
                gen()
            elif choice == 2:
                verifier()
            elif choice == 3:
                base64_gen()
            elif choice == 4:
                marshal_operations()
            elif choice == 0:
                print(cyan + "\nThanks For Using This Program" + reset)
            else:
                print(cyan + "\n Wrong Input ! , Try again" + reset)
                time.sleep(2)
                main()
        except ValueError:
            print(red + "Error: Please enter a valid option (numeric value)." + reset)

    except Exception as e:
        print(yellow + "\n[" + red + "Error" + yellow + "]" + cyan + f" Something went wrong! {e}. Please try again after some time." + reset)
        error_msg = input(cyan + "Press any key to Close the program ..." + reset)

if __name__ == "__main__":
    main()
    
