#Write a python script to determine whether a string contains a specific substring.

s1= "Anamikaa"
result=(s1.find("kaa"))
if result == -1:
    print("String doesn't contain the substring 'kaa'")
else:
    print("string contains the substring kaa starting at index", result)
