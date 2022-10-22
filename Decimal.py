word = '32'
print(word.isdecimal())
#output: True

word = '954'
print(word.isdecimal())
#output: True

print("\u2083".isdecimal()) #unicode for subscript 3
#output: False

word = 'beach'
print(word.isdecimal())
#output: False

word = 'number32'
print(word.isdecimal())
#output: False

word = '1 2 3' #notice the space between chars
print(word.isdecimal())
#output: False

word = '@32$' #notice the special chars '@' and '$'
print(word.isdecimal())
#output: False