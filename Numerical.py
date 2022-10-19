word = '32'
print(word.isnumeric())
#output: True

print("\u2083".isnumeric()) #unicode for subscript 3
#output: True

print("\u2169".isnumeric()) #unicode for roman numeral X
#output: True

word = 'beach'
print(word.isnumeric())
#output: False

word = 'number32'
print(word.isnumeric())
#output: False

word = '1 2 3' #notice the space between chars
print(word.isnumeric())
#output: False

word = '@32$' #notice the special chars '@' and '$'
print(word.isnumeric())
#output: False
