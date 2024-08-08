

def char_to_binary(char):
  ascii_value = ord(char)
  binary_representation = bin(ascii_value)[2:]
  return f'{binary_representation:08}'

char = 'B'
binary = char_to_binary(char)
print(f'The binary representation of {char} is {binary}')
