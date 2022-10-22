word = 'beach'
print(word.isalpha())
#output: True

word = '32'
print(word.isalpha())
#output: False

word = 'number32'
print(word.isalpha())
#output: False

word = 'Favorite number is blue' #notice the space between words
print(word.isalpha())
#output: False

word = '@beach$' #notice the special chars '@' and '$'
print(word.isalpha())
#output: Falseg