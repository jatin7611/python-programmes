import re
s = input("enter a string : ")
print("String befor removing multiple spaces:")
print(s)
print("String after removing multiple spaces:")
print(re.sub(' +', ' ', s)) 