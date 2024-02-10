b = "Hello world"
print(b[2:])
print(b[-1])
print(b[1:5])

# Modification of strings
a = "he is not a GooD boy"
print(a.upper())
print(a.lower())
print(a.strip()) # Removes any white spaces from the beginning or ending
print(a.replace("h", "Sh")) # h will be replaced by Sh

# format() used to insert the numbers into the strings
txt = "He is from hyderabad which is {} km from vijayawada"
distance = 500
print(txt.format(distance))

quantity = 10
itemno = 124
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

txt1 = "We are the so-called \"Vikings\" from the north."
print(txt1)
txt2 = "We are the so-called from the north india.\n but i live in south india"
print(txt2)





