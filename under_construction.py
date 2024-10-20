

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encode(text, shift):
#   new_text = ""
#   for letter in text:
#     if letter == " ":
#       new_text += " "
#     else:
#       letter = alphabet.index(letter)
#       encrypted_index = letter + shift
#       encrypted_index %= len(alphabet)     
#       new_text += alphabet[encrypted_index]
#   print(f"Here's the encoded result: {new_text}")

# def decode(text):
#   new_text = ""
#   for letter in text:
#     if letter == " ":
#       new_text += " "
#     else:
#       letter = alphabet.index(letter)
#       encrypted_index = letter - shift
#       if encrypted_index > len(alphabet) - 1:
#         encrypted_index -= len(alphabet)     
#       new_text += alphabet[encrypted_index]
#   print(f"Here's the decoded result: {new_text}")

def caesar(direction, text, shift):
  new_text = ""
  for letter in text:
    if letter == " ":
      new_text += " "
    else:
      letter = alphabet.index(letter)
      if direction == "encode":
        chosen_index = letter + shift
      else:
        chosen_index = letter - shift
      chosen_index %= len(alphabet)
      new_text += alphabet[chosen_index]
  print(f"Here's the result: {new_text}")      

run_again = "yes"
while run_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(direction, text, shift)
  run_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()