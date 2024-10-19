list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = "feliz"
shift = 1
new_word = ""
for item in word:
  if item == " ":
    new_word += " "
  else:
    actual_ind = list.index(item)
    new_ind = actual_ind + shift
    if new_ind > len(list)-1:
      new_ind -= len(list)
      new_word += list[new_ind]
    else:
      new_word += list[new_ind]

print(new_word)

print(len(list))
