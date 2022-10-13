word = input("Enter letters(without space): ")
count = len(word)
ct = 1
for i in word : 
    ct *= count
    count -= 1

print("Possible words are : ",ct)    
