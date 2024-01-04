import marshal
import uncompyle6

def decode_and_save(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            encoded_script = f.read()

        # Load the marshal-encoded data
        code_object = marshal.loads(encoded_script)

        # Use uncompyle6 to decompile the code object to source code
        decompiled_code = uncompyle6.decompile_code(code_object)

        # Save the decompiled code to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decompiled_code)

        print(f"Decoded script saved to {output_file}")
    except Exception as e:
        print(f"Error decoding script: {e}")

# Take input for marshal-encoded file and output file
input_file = input("Enter the Python 3 marshal-encoded file path: ")
output_file = input("Enter the output file path to store the decoded script: ")

decode_and_save(input_file, output_file)
