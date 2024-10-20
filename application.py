alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  output_text = ""
  for letter in text:
    if letter not in alphabet:
      output_text += letter
    else:
      letter = alphabet.index(letter)
      if direction == "encode":
        chosen_position = letter + shift
      else:
        chosen_position = letter - shift
      chosen_position %= len(alphabet)
      output_text += alphabet[chosen_position]
  print(f"Here's the {direction}d result: {output_text}")      

run_again = "yes"
print("------- Welcome to Caesar Cipher -------")
while run_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(direction, text, shift)
  run_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()