import marshal
import uncompyle6

def decode_and_save():
    try:
        # Ask the user for input file name
        input_file = input("Enter the name of the encoded marshal data file: ")

        # Read encoded data from input file
        with open(input_file, 'rb') as file:
            encoded_data = file.read()

        # Decode data using marshal
        decoded_data = marshal.loads(encoded_data)

        # Ask the user for output file name
        output_file = input("Enter the name of the file to save the decoded data: ")

        # Use uncompyle6 to decompile bytecode to source code
        source_code = uncompyle6.deparse_code(decoded_data, version=3.10)

        # Save decoded source code to output file
        with open(output_file, 'w') as file:
            file.write(source_code)

        print(f"Decoded data saved to {output_file}")
    except Exception as e:
        print(f"Decoding failed: {e}")

# Call the function
decode_and_save()
