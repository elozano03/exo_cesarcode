l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
word = "z" 
offset = 1
new_word = ""

for i in range(len(word)):
    the_letter = word[i]
    position_in_l = l.index(word[i])
    new_position = (position_in_l + offset) %26
    new_letter = l [new_position ]
    new_word += new_letter

    # new_word = new_word + l[(l.index(word[i])+offset)%26]

print(new_word)
    
    
