import marshal
import subprocess

def decode_and_save(input_file, output_file):
    temp_file = 'temp.py'  # Initialize the temp_file variable outside the try block
    
    try:
        with open(input_file, 'rb') as f:
            encoded_script = f.read()

        # Load the marshal-encoded data
        code_object = marshal.loads(encoded_script)

        # Write the code object to the temporary file
        with open(temp_file, 'w', encoding='utf-8') as file:
            file.write(repr(code_object))

        # Use uncompyle6 tool to decompile the temporary file
        subprocess.run(['uncompyle6', temp_file], stdout=open(output_file, 'w', encoding='utf-8'))

        print(f"Decoded script saved to {output_file}")
    except Exception as e:
        print(f"Error decoding script: {e}")
    finally:
        # Cleanup: remove the temporary file
        subprocess.run(['rm', temp_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Take input for marshal-encoded file and output file
input_file = input("Enter the Python 3.11 marshal-encoded file path: ")
output_file = input("Enter the output file path to store the decoded script: ")

decode_and_save(input_file, output_file)
