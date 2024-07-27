def letter_to_binary(letter):
    # Get ASCII value of the letter
    ascii_value = ord(letter)
    print(f"ASCII value of {letter}: {ascii_value}")
    # Convert ASCII value to binary string and remove '0b' prefix
    binary_value = bin(ascii_value)[2:]
    print(f"Binary value of {letter} (without padding): {binary_value}")
    # Ensure the binary string has 8 bits by padding with leading zeros
    binary_value = binary_value.zfill(8)
    return binary_value

char = input("Enter a letter you would like output as binary: ")

binary_value = letter_to_binary(char)

print(f"The binary value of {char} is {binary_value}")
