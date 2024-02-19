# It removes the extra whitespaces, if we specify the exact char or a symbol, it removes all the given symbols and give us the string 
# Note : it removes the characters from only beginning or at the end only not in the middle 

text = "---Hello, World???"

stripped_text = text.strip("-?")
print(stripped_text)

text1 = "!!!!!!!hello, #####world!!!!!!"
x = text1.strip("!")
print(x)
print(x.strip("#"))

text3 = "!!!!!!!hello, #####world!!!!!!"

# Replace "!" with an empty string to remove it
text4 = text3.replace("!", "")

# Replace "#" with an empty string to remove it
result = text4.replace("#", "")

print(result)