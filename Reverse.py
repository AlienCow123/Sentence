x = input("Enter a word which is to be reversed : ")
y = len(x)-1
b = ""
s = []
h = 0
#print(x[y])
while y>=0 :
    s.append(x[y])
    b += s[h]
    y -= 1
    h += 1
print(b)    

